import platform
import sys

if __name__ == '__main__':
    print('interpreter: ', platform.architecture())
    print('/bin/ls: ', platform.architecture('/bin/ls'))
