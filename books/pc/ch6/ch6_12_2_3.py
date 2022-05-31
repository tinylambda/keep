import struct

from ch6_12_2_2 import StructField


class NestedStruct:
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            data = instance._buffer[
                self.offset : self.offset + self.struct_type.struct_size
            ]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        fields = getattr(cls, "_fields_", [])
        byte_order = ""
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(cls, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(("<", ">", "!", "@")):
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


class Point(Structure):
    _fields_ = [("<d", "x"), ("d", "y")]


class PolyHeader(Structure):
    _fields_ = [
        ("<i", "file_code"),
        (Point, "min"),
        (Point, "max"),
        ("i", "num_polys"),
    ]


if __name__ == "__main__":
    with open("/tmp/polys.bin", "rb") as f:
        phead = PolyHeader.from_file(f)
        print(phead.file_code == 0x1234)
        print(phead.min)
        print(phead.min.x)
        print(phead.min.y)
        print(phead.max.x)
        print(phead.max.y)
        print(phead.num_polys)
