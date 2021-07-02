import aiohttp
import asyncio


# we define the get() function as asynchronous, so it is technically a coroutine
async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

loop = asyncio.get_event_loop()

# The eight coroutines are started and provided to the event loop at the same time
# and it is asyncio's job to schedule them efficiently.
coroutines = [get('http://example.com') for _ in range(8)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
print('results: %s' % results)

