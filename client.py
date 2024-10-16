import asyncio
import websockets

total = 0

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10000):
            global total
            message = f"Request {i}"
            await websocket.send(message)
            response = await websocket.recv()
            total += 1
            print(f"Response for {response}")

asyncio.run(send_message())

print(total)