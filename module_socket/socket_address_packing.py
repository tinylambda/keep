import binascii
import socket

for string_address in ["127.0.0.1", "10.1.1.2"]:
    packed = socket.inet_aton(string_address)
    print(f"origin {string_address}")
    print(f"packed {binascii.hexlify(packed)}")
    print(f"unpacked {socket.inet_ntoa(packed)}")
    print()
