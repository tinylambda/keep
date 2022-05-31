import urllib.parse

if __name__ == "__main__":
    url = "http://example.com:8000/pa/th;param1=foo;param2=bar?name=val#frag"
    print(urllib.parse.urlsplit(url))
    print(urllib.parse.urlparse(url))
