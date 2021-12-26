import os


if __name__ == '__main__':
    print(f'Starting: {os.getcwd()}')
    print(f'Moving up one: {os.pardir}')
    os.chdir(os.pardir)

    print(f'After move: {os.getcwd()}')
