import sys
import json
import asyncio
import websockets

from typing import List


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


def get_stdin(q):
    asyncio.ensure_future(q.put(sys.stdin.readline()))


async def simple_echo_client(uri: str, stdin_q: asyncio.Queue, stdout_q: asyncio.Queue):
    bye = False
    print(">>> ")
    async with websockets.connect(uri) as websocket:

        stdin_q_input_task: asyncio.Task = asyncio.get_event_loop().create_task(
            stdin_q.get()
        )
        stdin_q_input_task.add_done_callback(lambda x: print("1>>> "))
        ws_recv_task: asyncio.Task = asyncio.get_event_loop().create_task(
            websocket.recv()
        )
        ws_recv_task.add_done_callback(lambda x: print(x.result(), "\n2>>> "))

        tasks: List[asyncio.Task] = [stdin_q_input_task, ws_recv_task]

        print("Time to chat with others in the same room: ")
        await websocket.send(json.dumps({"message": "start chat"}))

        while True:
            for next_to_complete in asyncio.as_completed(tasks):
                await next_to_complete

                for t in tasks:
                    if not t.done():
                        t.set_result(None)

            stdin_q_input_task: asyncio.Task = asyncio.get_event_loop().create_task(
                stdin_q.get()
            )
            stdin_q_input_task.add_done_callback(lambda x: print(">>> "))
            ws_recv_task: asyncio.Task = asyncio.get_event_loop().create_task(
                websocket.recv()
            )
            ws_recv_task.add_done_callback(lambda x: print(x.result(), "\n>>> "))

            tasks: List[asyncio.Task] = [stdin_q_input_task, ws_recv_task]

        # while not bye:
        #     _input = input('> ')
        #     _input = _input.strip()
        #     await websocket.send(json.dumps({
        #         'message': _input
        #     }))
        #     echoed = await websocket.recv()
        #     print(f'< {echoed}')
        #
        #     if _input == 'bye':
        #         bye = True
        #         await websocket.close(code=1000, reason='Client Done')
        #
        # print('Bye')


event_loop = asyncio.get_event_loop()
in_q = asyncio.Queue()
out_q = asyncio.Queue()
event_loop.add_reader(sys.stdin, get_stdin, in_q)

try:
    event_loop.run_until_complete(
        simple_echo_client(
            uri="ws://localhost:20000/ws/chat/cc/", stdin_q=in_q, stdout_q=out_q
        )
    )
finally:
    event_loop.close()
