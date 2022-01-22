import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    pprint.pprint(psutil.virtual_memory())

    # total: total physical memory (exclusive swap).

    # available: the memory that can be given instantly to processes without the system going into swap.

    # used: memory used, calculated differently depending on the platform and designed for informational purposes only.
    # total - free does not necessarily match used.

    # free: memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the
    # actual memory available (use available instead). total - used does not necessarily match free.

    # active (UNIX): memory currently in use or very recently used, and so it is in RAM.

    # inactive (UNIX): memory that is marked as not used.

    # buffers (Linux, BSD): cache for things like file system metadata.

    # cached (Linux, BSD): cache for various things

    # shared (Linux, BSD): memory that may be simultaneously accessed by multiple processes.

    # slab (Linux): in-kernel data structures cache.
    