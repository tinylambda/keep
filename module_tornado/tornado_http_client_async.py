import asyncio
import functools
from asyncio import Future

import tornado.ioloop
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


async def asynchronous_fetch(url):
    print("fetching", url)
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    print("fetched", response.body)
    return response.body


@gen.coroutine
def asynchronous_fetch_old(url):
    print("fetching", url)
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    print("fetched", response.body)
    return response.body
    # for old version Python
    # raise gen.Return(response.body)


if __name__ == "__main__":
    test_url = "https://www.baidu.com/"

    def cb(f: Future, use_loop: tornado.ioloop.IOLoop):
        print(f.result())
        use_loop.stop()

    print("Normal")
    loop = tornado.ioloop.IOLoop.current()
    loop.add_future(
        asyncio.ensure_future(asynchronous_fetch(test_url)),
        functools.partial(cb, use_loop=loop),
    )
    loop.start()

    loop = tornado.ioloop.IOLoop.current()
    loop.add_future(
        asynchronous_fetch_old(test_url), functools.partial(cb, use_loop=loop)
    )
    loop.start()

    print("Using run_sync")
    loop.run_sync(lambda: asynchronous_fetch(test_url))
    loop.run_sync(lambda: asynchronous_fetch_old(test_url))
