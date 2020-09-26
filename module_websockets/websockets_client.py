import json
import asyncio
import websockets


# async def hello(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(json.dumps({
#             'message': 'Hello world!',
#         }))
#         msg = await websocket.recv()
#         print(f'< {msg}')
#
# asyncio.get_event_loop().run_until_complete(
#     hello('ws://localhost:20000/ws/chat/cc/')
# )

def mark_done(future, result):
    future.set_result(result)


async def simple_echo_client(uri):
    bye = False
    async with websockets.connect(uri) as websocket:
        while not bye:
            _input = input('> ')
            _input = _input.strip()
            await websocket.send(json.dumps({
                'message': _input
            }))
            echoed = await websocket.recv()
            print(f'< {echoed}')

            if _input == 'bye':
                bye = True
                await websocket.close(code=1000, reason='Client Done')

        print('Bye')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(simple_echo_client(uri='ws://localhost:20000/ws/chat/cc/'))
finally:
    event_loop.close()

