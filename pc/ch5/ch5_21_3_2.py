import time
import threading


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.setDaemon(True)
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


if __name__ == '__main__':
    countdown = Countdown(30)

    time.sleep(5)

    f = open('/tmp/state.p', 'wb')
    import pickle
    pickle.dump(countdown, f)
    f.close()

