import asyncio


async def coro():
    print("starting")
    await asyncio.sleep(2)
    print("done sleep")


async def cancel_it(some_task):
    await asyncio.sleep(0.5)
    some_task.cancel()
    print("cancellation effected")


async def main():
    _loop = asyncio.get_event_loop()
    real_task = _loop.create_task(coro())
    real_task.set_name("XXX task")
    shield = asyncio.shield(real_task)
    # cancel the shield in the background while we're waiting
    _loop.create_task(cancel_it(shield))
    print(real_task.get_name())
    await real_task

    assert not real_task.cancelled()
    assert shield.cancelled()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
