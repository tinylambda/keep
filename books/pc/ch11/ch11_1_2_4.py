import json
import pprint

import requests


if __name__ == "__main__":
    url = "http://httpbin.org/post"

    params = {
        "name1": "value1",
        "name2": "value2",
    }

    headers = {
        "User-Agent": "good/felix",
        "Content-Type": "application/json;charset=utf-8",
    }

    resp = requests.post(url, data=json.dumps(params), headers=headers)
    pprint.pprint(resp.json())
