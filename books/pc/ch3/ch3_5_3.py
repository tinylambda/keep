import struct


if __name__ == "__main__":
    data = b"\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004"
    hi, lo = struct.unpack(">QQ", data)
    print((hi << 64) + lo)

    print("-" * 64)

    x = 0x01020304
    print(x.to_bytes(4, "big"))

    print(x.to_bytes(4, "little"))

    print("-" * 64)

    x = 523**23
    print(x)

    # x.to_bytes(16, 'little')
    print(x.bit_length())

    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, "little"))
