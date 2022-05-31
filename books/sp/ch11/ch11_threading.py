import random
import threading


results = []


def compute(x):
    results.append(
        "%s - %s" % (x, sum([random.randint(1, 100) for i in range(1000000)]))
    )


workers = [threading.Thread(target=compute, args=(x,)) for x in range(8)]
for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

print("result: %s" % results)
