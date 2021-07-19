import json
import pprint
from urllib import request, parse


if __name__ == '__main__':
    url = 'http://httpbin.org/post'

    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    query_string = parse.urlencode(params)
    u = request.urlopen(url, data=query_string.encode('utf-8'))
    resp = u.read()
    pprint.pprint(json.loads(resp))
