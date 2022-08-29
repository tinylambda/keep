import secrets

if __name__ == "__main__":
    print(secrets.token_bytes(nbytes=16))
    print(secrets.token_hex(nbytes=16))
    print(secrets.token_urlsafe(nbytes=16))
