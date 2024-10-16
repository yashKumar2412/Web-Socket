import asyncio
from websockets.server import serve
import random

async def handle_client(websocket):
    async for message in websocket:
        random_number = random.randint(1, 100)
        modified_message = f"{message}: {random_number}"
        await websocket.send(modified_message)

async def main():
    async with serve(handle_client, "localhost", 8765):
        await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
