import asyncio


async def ioloop():
    event = {"biz": "battle", "biz_id": "1001"}
    biz = event.get("biz")
    if biz == "battle":
        from biz_battle import battle

        coro = battle()
        coro.send(None)
    else:
        raise RuntimeError("no such biz")

    biz_id = event.get("biz_id")
    io_event = coro.send(biz_id)
    print("got io_event: ", io_event)

    while True:
        try:
            io_event = coro.send("ok")
            print("got io_event: ", io_event)
        except StopIteration:
            print("StopIteration! bye!")
            break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ioloop())
