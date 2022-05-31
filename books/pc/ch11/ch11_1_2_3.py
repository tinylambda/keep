import json
import pprint
from urllib import request, parse


if __name__ == "__main__":
    url = "http://httpbin.org/post"

    headers = {"User-agent": "good/felix", "Content-Type": "application/json"}

    params = {
        "name1": "value1",
        "name2": "value2",
    }

    query_string = parse.urlencode(params)
    r = request.Request(url, data=json.dumps(params).encode("utf-8"), headers=headers)
    u = request.urlopen(r)
    resp = u.read()
    pprint.pprint(json.loads(resp))
