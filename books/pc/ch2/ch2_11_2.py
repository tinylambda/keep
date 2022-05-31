if __name__ == "__main__":
    s = " hello world \n"
    print(s.strip())

    print(s.lstrip())

    print(s.rstrip())

    t = "-----hello====="
    print(t.lstrip("-"))
    print(t.strip("-="))
