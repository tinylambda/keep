import threading

# Python builtin data types access is thread safe
DATA = {}


def add_data(inc=1):
    for i in range(1, 11):
        key = i + inc
        print(f'{threading.current_thread().getName()} Adding: ', key)
        DATA[key] = key


t1 = threading.Thread(target=add_data, args=(1, ))
t2 = threading.Thread(target=add_data, args=(100, ))

threads = [t1, t2]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(DATA)
print(len(DATA))
print('Done!')

