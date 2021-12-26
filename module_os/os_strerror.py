import errno
import os


if __name__ == '__main__':
    for num in [errno.ENOENT, errno.EINTR, errno.EBUSY]:
        name = errno.errorcode[num]
        print(f'[{num:>2}] {name:<6}: {os.strerror(num)}')
