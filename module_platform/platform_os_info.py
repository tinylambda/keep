import platform

if __name__ == '__main__':
    print('uname: ', platform.uname())
    print()

    print('system: ', platform.system())
    print('node: ', platform.node())
    print('release: ', platform.release())
    print('version: ', platform.version())
    print('machine: ', platform.machine())
    print('processor: ', platform.processor())
