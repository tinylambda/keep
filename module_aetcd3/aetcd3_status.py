import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def main():
    async with aetcd3.client() as client:
        status = await client.status()
        logging.info("leader: %s", status.leader)
        logging.info("version: %s", status.version)
        logging.info("raft_index: %s", status.raft_index)
        logging.info("raft_term: %s", status.raft_term)
        logging.info("db_size: %s", status.db_size)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
