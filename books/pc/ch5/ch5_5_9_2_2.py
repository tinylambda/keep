record_size = 32

buf = bytearray(record_size)
with open('ch5_9_2.py', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break

print(buf)

