import asyncio
import sys

from module_websockets.websockets_client2 import get_stdin, simple_ws

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    events_q = asyncio.Queue()
    event_loop.add_reader(sys.stdin, get_stdin, events_q)

    def on_error(e):
        print('error', e)
        sys.exit(1)

    asyncio.get_event_loop().run_until_complete(simple_ws(
        uri='ws://localhost:8000/ws/chat/cc/',
        on_open=lambda: print('open'),
        on_message=lambda msg: print('Received: ', msg),
        on_error=on_error,
        eq=events_q,
    ))
