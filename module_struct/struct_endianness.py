import struct
import binascii


values = (1, "ab".encode("utf-8"), 2.7)
print("Original values: ", values)

endianness = [
    ("@", "native, native"),
    ("=", "native standard"),
    ("<", "little-endian"),
    (">", "big-endian"),
    ("!", "network"),
]

for code, name in endianness:
    s = struct.Struct(code + " I 2s f")
    packed_data = s.pack(*values)
    print()
    print("Format string: ", s.format)
    print("Uses: ", s.size, "bytes")
    print("Packed Value: ", binascii.hexlify(packed_data))
    print("Unpacked Value: ", s.unpack(packed_data))


"""
@ 	Native order
= 	Native standard
< 	little-endian
> 	big-endian
! 	Network order
"""
