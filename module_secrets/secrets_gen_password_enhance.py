import secrets
import string

if __name__ == "__main__":
    alphabet = string.ascii_letters + string.digits
    while True:
        print("gen password")
        password = "".join(secrets.choice(alphabet) for i in range(10))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            break

    print(password)
