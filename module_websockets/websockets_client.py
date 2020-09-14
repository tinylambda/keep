import json
import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            'message': 'Hello world!',
        }))
        msg = await websocket.recv()
        print(f'< {msg}')

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:20000/ws/chat/cc/')
)

