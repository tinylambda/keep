import pprint

import requests


if __name__ == "__main__":
    resp = requests.head("http://www.python.org/index.html")

    pprint.pprint(resp.headers)
    status = resp.status_code
    content_length = resp.headers["content-length"]

    print(status, content_length)

    resp = requests.get(
        "http://pypi.python.org/pypi?:action=login", auth=("user", "password")
    )
    print(resp.text)

    resp1 = requests.get("http://www.baidu.com")
    resp2 = requests.get("http://www.bing.com", cookies=resp1.cookies)
    print(resp2.text)

    url = "http://httpbin.org/post"
    files = {"file": ("data.py", open("ch11_1_2_6.py", "rb"))}
    r = requests.post(url, files=files)
    pprint.pprint(r.json())
