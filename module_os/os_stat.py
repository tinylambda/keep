import os
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = __file__
    else:
        filename = sys.argv[1]

    stat_info = os.stat(filename)

    print(f'os.stat({filename})')
    print(f'\tSize: {stat_info.st_size}')
    print(f'\tPermissions: {stat_info.st_mode}')
    print(f'\tOwner: {stat_info.st_uid}')
    print(f'\tDevice: {stat_info.st_dev}')
    print(f'\tCreated: {time.ctime(stat_info.st_ctime)}')
    print(f'\tLast modified: {time.ctime(stat_info.st_mtime)}')
    print(f'\tLast accessed: {time.ctime(stat_info.st_atime)}')
