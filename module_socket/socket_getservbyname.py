import socket
from urllib.parse import urlparse


URLS = [
    'http://www.python.org',
    'https://www.baidu.com',
    'ftp://prep.ai.mit.edu',
    'pop3://pop.example.com',
    'pop3s://pop.example.com',
]


if __name__ == '__main__':
    for url in URLS:
        parsed_url = urlparse(url)
        port = socket.getservbyname(parsed_url.scheme)
        print(f'{parsed_url.scheme:>6}: {port}')
