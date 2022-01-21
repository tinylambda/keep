import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def on_terminate(proc):
    print('process {} terminated with exit code {}'.format(proc, proc.returncode))


if __name__ == '__main__':
    procs = psutil.Process().children()

    for p in procs:
        p.terminate()

    gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
    for p in alive:
        p.kill()
