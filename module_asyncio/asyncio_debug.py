import argparse
import asyncio
import logging
import sys
import time
import warnings


parser = argparse.ArgumentParser("debugging asyncio")
parser.add_argument(
    "-v",
    dest="verbose",
    default=False,
    action="store_true",
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s: %(message)s",
    stream=sys.stderr,
)
LOG = logging.getLogger("")


async def inner():
    LOG.info("inner starting")
    time.sleep(0.1)
    LOG.info("inner complete")


async def outer(loop):
    LOG.info("outer starting")
    await asyncio.ensure_future(loop.create_task(inner()))
    LOG.info("outer completed")


event_loop = asyncio.get_event_loop()
if args.verbose:
    LOG.info("enabling debugging")
    event_loop.set_debug(True)

    event_loop.slow_callback_duration = 0.001

    warnings.simplefilter("always", ResourceWarning)

event_loop.run_until_complete(outer(event_loop))
