import os
import sys
import time


if __name__ == '__main__':
    workers = []
    for i in range(2):
        print(f'PARENT {os.getpid()}: Forking {i}')
        worker_pid = os.fork()
        if not worker_pid:
            print(f'WORKER {i}: Starting')
            time.sleep(2 + i)
            print(f'WORKER {i}: Finishing')
            sys.exit(i)
        workers.append(worker_pid)

    for pid in workers:
        print(f'PARENT :Waiting for {pid}')
        done = os.waitpid(pid, 0)
        print(f'PARENT: Child done: {done}')
