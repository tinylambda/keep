import asyncio
import logging


async def problem():
    await asyncio.sleep(1)
    logging.warning("going to raise an exception now!")
    raise RuntimeError("something went wrong")


def exception_handler(my_loop, context):
    print('get exception...')


async def main():
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)

    task = loop.create_task(problem())
    logging.info('created task = %r', task)
    tasks = [task]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for t in tasks:
        if t.done():
            print(t, 'done')
            # t.exception()
            # exception = t.exception()
            # if exception is not None:
            #     print('exception just happened')
            # else:
            #     result = t.result()
            #     print('get result', result)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(filename)s:%(lineno)d %(levelname)s %(message)s',
        level=logging.INFO,
        datefmt='%H:%M:%S'
    )
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.info('closing the loop')
        loop.close()

    logging.info('shutting down')

