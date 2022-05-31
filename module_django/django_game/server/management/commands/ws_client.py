import os
import sys
import json
import signal
import typing
import asyncio
import websockets
import urllib
import urllib.parse

from django.core.management.base import BaseCommand, CommandError


def get_stdin_data(q):
    """data from stdin"""
    asyncio.ensure_future(q.put(sys.stdin.readline()))


async def simple_ws(
    uri: typing.AnyStr,
    on_open: typing.Callable = None,
    on_message: typing.Callable = None,
    on_error: typing.Callable = None,
    q: asyncio.Queue = None,
):
    """a simple WebSocket client"""

    def call_function(f, *args):
        if f:
            f(*args)

    loop = asyncio.get_event_loop()
    async with websockets.connect(uri, extra_headers=[]) as client_side_ws:
        call_function(on_open)
        i = 0

        def create_input_task():
            _task = loop.create_task(q.get())
            _task.set_name("input")
            return _task

        def create_recv_task():
            _task = loop.create_task(client_side_ws.recv())
            _task.set_name("recv")
            return _task

        task_creation_callables = [
            create_input_task,
            create_recv_task,
        ]

        while True:
            try:
                tasks = [f() for f in task_creation_callables]
                await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

                for i, task in enumerate(tasks):
                    if task.done():
                        task_name = task.get_name()
                        if task_name == "input":
                            user_input = task.result().strip()
                            user_input_bytes: bytes = user_input.encode("utf-8")
                            await client_side_ws.send(user_input_bytes)
                        elif task_name == "recv":
                            msg_bytes: bytes = task.result()
                            msg = json.loads(msg_bytes)
                            call_function(on_message, msg)

                            if msg is not None:
                                content = msg.get("content")
                                if content and content.strip() == "bye":
                                    break

                        tasks[i] = task_creation_callables[i]()
            except Exception as e:
                call_function(on_error, e)
                break
            finally:
                for task in tasks:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass


class Command(BaseCommand):
    help = "Start a chat client"

    def add_arguments(self, parser):
        parser.add_argument(
            "ws_url",
            nargs="?",
            help="WebSocket url",
            type=str,
            default="ws://127.0.0.1:8000/ws/game/",
        )

    def handle(self, *args, **options):
        ws_url = options["ws_url"]

        loop = asyncio.get_event_loop()
        q = asyncio.Queue()
        loop.add_reader(sys.stdin, get_stdin_data, q)

        try:
            loop.run_until_complete(
                simple_ws(
                    uri=ws_url,
                    on_open=lambda: print("connected"),
                    on_message=lambda msg: print("Received: ", msg),
                    on_error=lambda e: print("Error: ", e),
                    q=q,
                )
            )
        except KeyboardInterrupt:
            pass
        self.stdout.write(self.style.SUCCESS("Done"))
