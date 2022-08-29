import secrets

if __name__ == "__main__":
    url = "https://example.com/reset=" + secrets.token_urlsafe()
    print(url)
