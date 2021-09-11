import socket

if __name__ == '__main__':
    hostname, aliases, addresses = socket.gethostbyaddr('127.0.0.1')
    print(f'hostname: {hostname}')
    print(f'aliases: {aliases}')
    print(f'addresses: {addresses}')
