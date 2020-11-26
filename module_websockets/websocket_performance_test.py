import asyncio
import json
import time

import websockets


async def test_task(ws_uri, msg):
    async with websockets.connect(ws_uri) as client_side_ws:
        await client_side_ws.send(msg)


async def performance_test(ws_uri=None, n=100):
    if ws_uri is None:
        return

    tasks = []
    for i in range(n):
        msg = json.dumps(
            {
                'message': f'MESSAGE {i}',
            }
        )

        t = asyncio.get_event_loop().create_task(test_task(ws_uri, msg))
        tasks.append(t)

    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(performance_test('ws://localhost:20000/ws/chat/cc/', 2000))
    print(f'Done after {time.time() - start} seconds')
