import struct

from ch6_12_2_3 import StructureMeta, PolyHeader, Point


class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        (sz,) = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off : off + size]
                yield code(data)


if __name__ == "__main__":
    with open("/tmp/polys.bin", "rb") as f:
        phead = PolyHeader.from_file(f)
        print(phead.num_polys)

        polydata = [SizedRecord.from_file(f, "<i") for n in range(phead.num_polys)]
        print(polydata)
        for n, poly in enumerate(polydata):
            print("polygon", n)
            for p in poly.iter_as("<dd"):
                print(p)

        print("-" * 64)

        for n, poly in enumerate(polydata):
            print("polygon", n)
            for p in poly.iter_as(Point):
                print(p.x, p.y)
