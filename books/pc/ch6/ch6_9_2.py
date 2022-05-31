import binascii
import base64


if __name__ == "__main__":
    s = b"hello"
    h = binascii.b2a_hex(s)
    print(h)

    print(binascii.a2b_hex(h))

    h = base64.b16encode(s)
    print(h)
    print(base64.b16decode(h))

    print(h.decode("ascii"))
