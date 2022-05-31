from urllib import parse
from urllib import request


if __name__ == "__main__":
    query_args = {"q": "query string", "foo": "bar"}
    encoded_args = parse.urlencode(query_args)
    print("Encoded: ", encoded_args)

    url = "http://localhost:8080/?" + encoded_args
    print(request.urlopen(url).read().decode("utf-8"))
