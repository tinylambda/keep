from urllib import request, parse


if __name__ == '__main__':
    url = 'http://httpbin.org/get'

    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    query_string = parse.urlencode(params)
    u = request.urlopen(url + '?' + query_string)
    resp = u.read()
    print(resp)
