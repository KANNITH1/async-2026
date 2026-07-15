import asyncio
import time
import httpx

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301041"
LIGHTS = ["light_1", "light_2", "light_3", "light_4"]

def reset_lights():
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/reset"
    try:
        response = httpx.delete(url)
        if response.status_code == 200:
            print("Reset all lights successfully.")
        else:
            print(f"Failed to reset lights: {response.status_code}")
    except Exception as e:
        print(f"Error resetting lights: {e}")

async def turn_on_single_light_async(client, light_id):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    await client.post(url, json={"status": "ON"})

async def turn_on_concurrent():
    print("\n--- Starting Concurrent Turn On (Async) ---")
    start_time = time.time()
    
    async with httpx.AsyncClient() as client:
        tasks = [turn_on_single_light_async(client, light_id) for light_id in LIGHTS]
        await asyncio.gather(*tasks)
        
    end_time = time.time()
    print(f"Concurrent Turn On Completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    reset_lights()
    time.sleep(1)  # รอระบบเคลียร์สถานะ 1 วินาที
    asyncio.run(turn_on_concurrent())