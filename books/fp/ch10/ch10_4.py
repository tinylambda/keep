from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = self.__class__
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))


if __name__ == "__main__":
    v = Vector([3.1, 4.2])
    print(v)

    v = Vector((3, 4, 5))
    print(v)

    v = Vector(range(100))
    print(v)

    print(len(v))
    print(
        v[0],
        v[1],
        v[2],
    )
    print(v[3:5])

    print(v[-1])
    print(v[1:4])
    print(v[-1:])
    print(v[1, 2])
