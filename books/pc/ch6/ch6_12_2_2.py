import struct

from ch6_12_2_1 import StructField


class StructureMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        fields = getattr(cls, "_fields_", [])
        byte_order = ""
        offset = 0

        for format, fieldname in fields:
            if format.startswith((">", "<", "!", "@")):
                byte_order = format[0]
                format = format[1:]

            format = byte_order + format
            setattr(cls, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(cls, "struct_size", offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ("<i", "file_code"),
        ("d", "min_x"),
        ("d", "min_y"),
        ("d", "max_x"),
        ("d", "max_y"),
        ("i", "num_polys"),
    ]


if __name__ == "__main__":
    with open("/tmp/polys.bin", "rb") as f:
        phead = PolyHeader.from_file(f)
        print(phead.file_code == 0x1234)
        print(phead.min_x)
        print(phead.min_y)
        print(phead.max_x)
        print(phead.max_y)
        print(phead.num_polys)
