from urllib import request


if __name__ == "__main__":
    r = request.Request("http://localhost:8080/")
    r.add_header("User-agent", "Felix (felix#github)")

    response = request.urlopen(r)
    data = response.read().decode("utf-8")
    print(data)
