from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name, result_queue):
    # ดึง PID ของหน่วยประมวลผลนี้ (ซึ่งจะแยกกันเด็ดขาด)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading. current_thread(). name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name} ] กำลังชงกาแฟให้ ลูกค้า {customer_name} ... ")
    start_cpu = process_time()
    sum(i * i for i in range(1000000) ) # จำลองงานคำนวณ (CPU-bound) เล็กน้อย และรอ 5 วินาที
    sleep(5) # บล็อกการทำงานของ Thread นี้ไว้ 5 วินาทีเต็มๆ
    cpu_duration = process_time() - start_cpu   
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name} ] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

# ส่งค่าการกิน RAM และ CPU ของตัวเองกลับไปให้หน่วยหลักผ่าน Queue
    process = psutil.Process(pid)
    mem_mb = process.memory_info().rss / (1024 * 1024)
    result_queue.put((mem_mb, cpu_duration))

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Multiprocessing === ")
    start_time = time()
    main_start = process_time()

    result_queue = multiprocessing.Queue()
    processes = []
    for customer in queue:
        process = multiprocessing.Process(target=make_coffee, args=(customer, result_queue))
        processes.append(process)
        process.start()

    child_mem_mb = []
    child_cpu_time = []    

    for _ in range(len(processes)):
        mem_mb, cpu_duration = result_queue.get()
        child_mem_mb.append(mem_mb)
        child_cpu_time.append(cpu_duration)
    
    for p in processes:
        p.join()

    duration = time() - start_time

    main_process = psutil.Process(main_pid)
    main_mem = main_process.memory_info().rss / (1024 * 1024)
    
    total_memory = main_mem + sum(child_mem_mb)
    total_cpu_time = (process_time() - main_start) + sum(child_cpu_time)

    print(f"[สรุปผล Multi-Process]")
    print(f"เวลาที่ใช้จริง (Wall Time) : {duration:0.2f} วินาที")
    print(f"เวลารวมที่ CPU ใช้ประมวลผลจริง (CPU Time) : {total_cpu_time:0.4f} วินาที")
    print(f"ทรัพยากร Memory (RAM) ที่ใช่: {total_memory: .2f} MB")

if __name__ == "__main__":
    main()      