import asyncio
import collections

import aiohttp
import aiohttp.web_exceptions
from aiohttp import web
import tqdm

from books.fp.ch17.flags2_common import main, HTTPStatus, Result, save_flag


DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


async def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    async with aiohttp.request('GET', url) as resp:
        if resp.status == 200:
            image = await resp.read()
            return image
        elif resp.status == 404:
            raise web.HTTPNotFound()
        else:
            raise web.HTTPError()


async def download_one(cc, base_url, semaphore, verbose):
    try:
        # control the number of coroutine started
        async with semaphore:
            image = await get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower() + '.gif')
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


async def download_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)]
    to_to_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_to_iter = tqdm.tqdm(to_to_iter, total=len(cc_list))
    for future in to_to_iter:
        try:
            res = await future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        counter[status] += 1
    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = download_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)




