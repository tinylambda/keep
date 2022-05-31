import asyncio
import functools
from asyncio import Future

from tornado.gen import multi, coroutine, convert_yielded
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


async def parallel_fetch(urls):
    http_client = AsyncHTTPClient()
    responses = await multi([http_client.fetch(url) for url in urls])
    return responses


@coroutine
def parallel_fetch_old(urls):
    http_client = AsyncHTTPClient()
    responses = yield [http_client.fetch(url) for url in urls]
    return responses


if __name__ == "__main__":
    test_urls = ["https://www.baidu.com/", "https://www.qq.com/"]
    loop = IOLoop.current()

    def cb(f: Future, use_loop: IOLoop):
        print([item.effective_url for item in f.result()])
        use_loop.stop()

    loop.add_future(
        asyncio.ensure_future(parallel_fetch(test_urls)),
        callback=functools.partial(cb, use_loop=loop),
    )
    loop.start()

    loop.add_future(
        convert_yielded(parallel_fetch(test_urls)),
        callback=functools.partial(cb, use_loop=loop),
    )
    loop.start()

    loop.add_future(
        parallel_fetch_old(test_urls), callback=functools.partial(cb, use_loop=loop)
    )
    loop.start()
