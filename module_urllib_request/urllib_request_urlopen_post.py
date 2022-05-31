from urllib import parse
from urllib import request


if __name__ == "__main__":
    query_args = {"q": "query string", "foo": "bar"}
    encoded_args = parse.urlencode(query_args).encode("utf-8")
    print("Encoded: ", encoded_args)

    url = "http://localhost:8080/"
    r = request.Request(
        url,
        data=encoded_args,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    print(request.urlopen(r).read().decode("utf-8"))
