from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


if __name__ == "__main__":
    test_url = "https://www.baidu.com/"
    print(synchronous_fetch(test_url))
