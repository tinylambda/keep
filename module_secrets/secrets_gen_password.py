import secrets
import string

if __name__ == "__main__":
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(8))
    print(password)
