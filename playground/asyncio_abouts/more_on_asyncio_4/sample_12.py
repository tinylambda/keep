import asyncio
import logging
import signal

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


async def cant_stop_me():
    logging.info('can not stop me...')
    for i in range(12):
        logging.info('sleeping for 5 seconds...')
        await asyncio.sleep(5)
    logging.info('done!')


async def parent_task():
    logging.info('kicking of shielded task')
    await asyncio.shield(cant_stop_me())
    logging.info('shield task done')


async def main():
    asyncio.create_task(parent_task())
    await asyncio.sleep(60)


async def shutdown(signal, loop):
    logging.info(f'received exit signal {signal.name}...')
    logging.info('closing database connections')
    logging.info('nacking outstanding messages')
    tasks = [t
             for t in asyncio.all_tasks()
             if t is not asyncio.current_task()
             ]
    for task in tasks:
        if task.get_coro().__name__ == 'cant_stop_me':
            continue
        task.cancel()
    logging.info(f'cancelling {len(tasks)} outstanding tasks')
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info('stopping loop')
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, loop)))

    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        logging.info('successfully shutdown service')
        loop.close()
