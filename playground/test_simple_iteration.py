import time

start = time.time()
i = 0
for i in range(10000000000):
    i += 1
    if i % 100000000 == 0:
        print(i)

print("cost time", time.time() - start, "secs")
