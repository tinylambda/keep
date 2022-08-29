import secrets

if __name__ == "__main__":
    with open("/usr/share/dict/words") as f:
        words = [word.strip() for word in f]
        password = " ".join(secrets.choice(words) for i in range(4))

    print(password)
