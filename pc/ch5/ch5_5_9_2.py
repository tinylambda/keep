import os.path


def read_into_buf(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


test_file_name = 'sample.bin'

if not os.path.exists(test_file_name):
    with open(test_file_name, 'wb') as f:
        f.write(b'Hello World')

buf = read_into_buf(test_file_name)
print(buf)

buf[0:5] = b'Hallo'
print(buf)

test_file_name_2 = 'newsample.bin'
with open(test_file_name_2, 'wb') as f:
    f.write(buf)

print(buf)

m1 = memoryview(buf)
print(m1)

m2 = m1[-5:]
print(m2)

m2[:] = b'WORLD'
print(buf)


