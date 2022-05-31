import asyncio
import json
import sys

import websockets

from typing import Callable


def get_stdin(eq):
    """Event from standard input"""
    e = {"type": "stdin", "value": sys.stdin.readline()}
    asyncio.ensure_future(eq.put(e))


# This is the main entrypoint of WebSocket app
async def simple_ws(
    uri: str,
    on_open: Callable = None,
    on_message: Callable = None,
    on_error: Callable = None,
    eq: asyncio.Queue = None,
):
    def _callback(f, *args):
        if f:
            f(*args)

    loop = asyncio.get_event_loop()
    async with websockets.connect(uri) as client_side_ws:
        _callback(on_open)
        while True:
            try:
                input_task = loop.create_task(eq.get())
                ws_recv_task = loop.create_task(client_side_ws.recv())
                tasks = [input_task, ws_recv_task]
                await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                if input_task.done():
                    e = input_task.result()
                    value = e.get("value")
                    parts = value.strip().split("|")
                    input_dict = dict(zip(parts[0::2], parts[1::2]))
                    print("User input: ", input_dict)
                    await client_side_ws.send(json.dumps(input_dict))

                msg = "{}"
                if ws_recv_task.done():
                    msg = ws_recv_task.result()
                    on_message(msg)

                for task in tasks:
                    task.cancel()

                msg_dict: dict = json.loads(msg)
                message = msg_dict.get("message")
                if message and message.strip() == "bye":
                    break
            except Exception as e:
                on_error(e)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    events_q = asyncio.Queue()
    event_loop.add_reader(sys.stdin, get_stdin, events_q)

    def on_error(e):
        print("Error: ", e)
        sys.exit()

    user_id = sys.argv[1]
    asyncio.get_event_loop().run_until_complete(
        simple_ws(
            uri=f"ws://localhost:20000/ws/game/{user_id}/",
            on_open=lambda: print("open"),
            on_message=lambda msg: print("Received: ", msg),
            on_error=lambda e: on_error(e),
            eq=events_q,
        )
    )
