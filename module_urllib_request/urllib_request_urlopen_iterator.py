from urllib import request


if __name__ == "__main__":
    response = request.urlopen("http://localhost:8080/")
    for line in response:
        print(line.decode("utf-8").rstrip())
