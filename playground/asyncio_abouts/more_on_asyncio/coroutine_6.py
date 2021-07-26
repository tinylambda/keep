import asyncio

from coroutines import f, g, g_sleep


async def main():
    for fut in asyncio.as_completed([g_sleep(2), f(), g()], timeout=5.0):
        try:
            await fut
            print('one task done')
        except Exception as e:
            print('ouch', e)

if __name__ == '__main__':
    asyncio.run(main())
