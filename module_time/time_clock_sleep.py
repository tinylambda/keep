import time


template = '{} - {:0.2f} - {:0.2f}'

print(template.format(
    time.time(), time.time(), time.process_time()
))

for i in range(3, 0, -1):
    print('Sleeping', i)
    time.sleep(i)
    print(template.format(
        time.ctime(), time.time(), time.process_time()
    ))

# Calling sleep() yields control from the current thread
# and asks it to wait for the system to wake it back up.

