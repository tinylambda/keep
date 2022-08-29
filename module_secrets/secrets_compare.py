import secrets

if __name__ == "__main__":
    a = "123"
    b = "456"

    r = secrets.compare_digest(a, b)
    print(r)

    a = "123"
    b = "123"
    r = secrets.compare_digest(a, b)
    print(r)
