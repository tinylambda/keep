import socket


if __name__ == '__main__':
    result = socket.getaddrinfo('www.baidu.com', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
    for res in sorted(result, key=lambda x: x[0]):
        print(res)

    print('-' * 64)

    result = socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
    for res in sorted(result, key=lambda x: x[0]):
        print(res)

    print('-' * 64)

    result = socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
    for res in sorted(result, key=lambda x: x[0]):
        print(res)
