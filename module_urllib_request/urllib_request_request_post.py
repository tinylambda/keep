from urllib import parse
from urllib import request


if __name__ == '__main__':
    query_args = {'q': 'query string', 'foo': 'bar'}
    r = request.Request(url='http://localhost:8080/', data=parse.urlencode(query_args).encode('utf-8'))
    print('Request method: ', r.get_method())
    r.add_header('User-agent', 'Felix # github')

    print()
    print('OUTGOING DATA: ')
    print(r.data)

    print()
    print('SERVER RESPONSE: ')
    print(request.urlopen(r).read().decode('utf-8'))
    