# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from os import name
from time import time, ctime
from tracemalloc import start


async def serve_customer(name):
    print(f"{ctime()}: Serving customer {name}...")
    await asyncio.sleep(1)  # Simulate a delay in serving the customer
    print(f"{ctime()}: --> Served {name}!")

async def main():
    start = time()
    await serve_customer("A")
    await serve_customer("B")    

    print(f"Total time taken: {time() - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())