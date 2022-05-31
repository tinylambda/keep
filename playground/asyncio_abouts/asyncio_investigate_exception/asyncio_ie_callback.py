import asyncio
import logging


def _handle_task_result(task: asyncio.Task):
    try:
        task.result()
    except asyncio.CancelledError:
        pass
    except Exception:
        logging.exception("exception raised by task = %r", task)


async def problem():
    await asyncio.sleep(1)
    logging.warning("going to raise an exception now!")
    raise RuntimeError("something went wrong")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d %(filename)s:%(lineno)d %(levelname)s %(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )

    loop = asyncio.get_event_loop()
    logging.info("creating the problem task")
    task = loop.create_task(problem())
    task.add_done_callback(_handle_task_result)
    logging.info("created task = %r", task)
    logging.info("running the loop")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("closing the loop")
        loop.close()

    logging.info("shutting down")
