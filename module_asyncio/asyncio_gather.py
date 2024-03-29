# If the background phases are well-defined, and only the results of those phases matter, then gather() may be more
# useful for waiting for multiple operations

import asyncio


async def phase1():
    print("in phase1")
    await asyncio.sleep(2)
    print("done with phase1")
    return "phase1 result"


async def phase2():
    print("in phase2")
    await asyncio.sleep(1)
    print("done with phase2")
    return "phase2 result"


async def main():
    print("starting main")
    print("waiting for phases to complete")
    results = await asyncio.gather(phase1(), phase2())
    print("results: {!r}".format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()
