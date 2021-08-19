import asyncio
import logging
import signal

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


async def cant_stop_me():
    logging.info('cannot stop me...')
    for i in range(12):
        logging.info('sleeping for 5 seconds...')
        await asyncio.sleep(5)
    logging.info('done!')


async def parent_task():
    # shielding should prevent `cant_stop_me` from cancellation if
    # `parent_task` gets cancelled (i.e. by `shutdown`)
    logging.info('kicking of shielded task')
    await asyncio.shield(cant_stop_me())
    logging.info('shielded task done')


async def main():
    asyncio.create_task(parent_task())
    await asyncio.sleep(60)


async def shutdown(sig, loop):
    logging.info(f'received exit signal {sig.name}...')
    tasks: list[asyncio.Task] = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for task in tasks:
        # skipping over shielded coroutine still does not help
        if task._coro.__name__ == 'cant_stop_me':
            continue
        task.cancel()
    logging.info('cancelling outstanding tasks')
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, loop)))

    try:
        loop.run_until_complete(main())
    finally:
        # Doing our cleanup in a finally clause isn’t enough,
        # though, since a signal could be sent outside of the try/except clause.
        logging.info('successfully shutdown service')
        loop.close()
