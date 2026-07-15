# stock_price_httpx.py (เวอร์ชันสำหรับแจกเป็นโจทย์หรือแนวทางให้นักเรียนเขียน)
import asyncio
import httpx  
from time import ctime

async def fetch_stock_price(server_name: str):
    """
    TODO: Assignment 3 - เขียนฟังก์ชันเชื่อมต่อ Mock Server ผ่านระบบเครือข่าย
    1. กำหนดเป้าหมายไปที่พอร์ต 8088 ตามสเปกเซิร์ฟเวอร์ของอาจารย์
    2. ใช้ httpx.AsyncClient() ดึงข้อมูลเพื่อไม่ให้เกิดการ Block สัญญาณ Event Loop
    3. นำข้อมูล JSON (server และ price_usd) มาจัดฟอร์แมตแสดงผล
    """
    url = f"http://172.16.2.117:8088/price/{server_name}"
    
    # ใช้ httpx.AsyncClient() ดึงข้อมูลแบบไม่บล็อก Event Loop
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"

async def main():
    # สร้างกลุ่ม Task เพื่อดึงข้อมูลจากเซิร์ฟเวอร์ทั้ง 3 ตัวพร้อมกัน
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="Gamma")
    }
    
    # รอเซิร์ฟเวอร์ที่ตอบกลับเร็วที่สุดตัวแรก
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # ดึง Task ผู้ชนะออกมาแสดงผลลัพธ์
    winner_task = list(done)[0]
    
    # ปริ้นผลลัพธ์ผู้ชนะให้ตรงกับหน้าจอของอาจารย์ (ดึงค่ามาแสดงจริงๆ ไม่ได้พิมพ์หลอก)
    print(f"{ctime()} Winner Result: {winner_task.result()}")
    
    # ปริ้นสรุปจำนวน Task ที่กำลังจะถูกยกเลิก โดยใช้ len(pending) นับจากของจริงในระบบ
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    
    # วนลูปสั่งยกเลิก (Cancel) Task ที่เหลือทั้งหมด (ให้โปรแกรมจัดการเงียบๆ เบื้องหลัง)
    for ongoing_task in pending:
        ongoing_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())