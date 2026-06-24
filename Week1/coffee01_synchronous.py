from time import sleep, ctime, time

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()}: เริ่มทำกาแฟให้ {customer_name}")
    print(f"{ctime()}: ทำกาแฟเสร็จสำหรับ {customer_name}")
    sleep(1)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"{ctime()}: กาแฟสำหรับ {customer_name} เรียบร้อย!")

def main():
    # คิวลูกค้า
    queue = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for customer in queue:
        make_coffee(customer)

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    