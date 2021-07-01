import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


sample_data_file = 'data.bin'
sample_data_size = 1000000
if not os.path.exists(sample_data_file):
    with open(sample_data_file, 'wb') as f:
        f.seek(sample_data_size-1)
        f.write(b'\x00')

m = memory_map(sample_data_file)
print(len(m))
print(m[0:10])
print(m[0])

m[:11] = b'Hello World'
m.close()

with open(sample_data_file, 'rb') as f:
    print(f.read(11))


with memory_map(sample_data_file) as m:
    print(len(m))
    print(m[0:11])

