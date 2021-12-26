import os
import signal
import time


def signal_usr1(signum, frame):
    pid = os.getpid()
    print(f'Received USR1 in process {pid}')


if __name__ == '__main__':
    print(f'Parent PID: {os.getpid()}')
    print('Forking')
    child_pid = os.fork()
    if child_pid:
        print('PARENT: Pausing before sending signal...')
        time.sleep(1)
        print(f'PARENT: Signaling {child_pid}')
        os.kill(child_pid, signal.SIGUSR1)
    else:
        print('CHILD: Setting up signal handler')
        signal.signal(signal.SIGUSR1, signal_usr1)
        print('CHILD: Pausing to wait for signal')
        time.sleep(5)
