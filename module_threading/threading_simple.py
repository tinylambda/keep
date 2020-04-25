import threading


def worker():
    print('Worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=())
    threads.append(t)
    t.start()

