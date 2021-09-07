import socket


HOSTS = [
    'apu',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
    'www.baidu.com',
]

if __name__ == '__main__':
    for host in HOSTS:
        print(host)
        try:
            name, aliases, addresses = socket.gethostbyname_ex(host)
            print(f'\thostname: {name}')
            print(f'\taliases: {aliases}')
            print(f'\taddresses: {addresses}')
        except socket.error as msg:
            print(f'error: {msg}')
        print()
