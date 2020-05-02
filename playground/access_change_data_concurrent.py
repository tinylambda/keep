import threading
import time

DATA = []


def add_data():
    for i in range(10):
        print('Adding: ', i)
        DATA.append(i)
        time.sleep(1)


def get_data():
    time.sleep(5)
    print('Access shared data: ')
    for i in DATA:
        print(i)


threads = []
t_adder = threading.Thread(target=add_data, args=())
t_getter = threading.Thread(target=get_data, args=())

threads.extend([t_adder, t_getter])
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('Done!')

