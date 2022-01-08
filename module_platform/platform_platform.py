import platform

if __name__ == '__main__':
    print('Normal: ', platform.platform())
    print('Aliased: ', platform.platform(aliased=True))
    print('Terse: ', platform.platform(terse=True))
