import asyncio
import aiohttp

from books.fp.ch17.ch17_1 import BASE_URL, save_flag, show, main


async def get_flag(cc):
    url = f"{BASE_URL}/{cc}/{cc}.gif"
    async with aiohttp.request("GET", url) as resp:
        image = await resp.read()
        return image


async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in cc_list]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == "__main__":
    main(download_many)
