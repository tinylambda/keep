import json
import pprint

import requests


if __name__ == '__main__':
    url = 'http://httpbin.org/post'

    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    resp = requests.post(url, json=params)
    pprint.pprint(resp.json())
