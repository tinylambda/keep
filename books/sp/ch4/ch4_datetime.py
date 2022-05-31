import datetime


if __name__ == "__main__":
    print(datetime.datetime.utcnow())
    print(datetime.datetime.utcnow().tzinfo is None)
    print(datetime.datetime.now())
