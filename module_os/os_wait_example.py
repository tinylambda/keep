import os
import sys
import time


if __name__ == "__main__":
    for i in range(2):
        print(f"PARENT {os.getpid()}: Forking {i}")
        worker_pid = os.fork()
        if not worker_pid:
            print(f"WORKER {i} Starting")
            time.sleep(2 + i)
            print(f"WORKER {i} Finishing")
            sys.exit(i)

    for i in range(2):
        print(f"{os.getpid()} PARENT: Waiting for {i}")
        done = os.wait()
        print(f"{os.getpid()} PARENT: Child done {done}")
