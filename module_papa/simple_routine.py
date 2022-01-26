import sys
import time

if __name__ == '__main__':
    for i in range(10):
        print('Got', i)
        sys.stdout.flush()
        time.sleep(1)
