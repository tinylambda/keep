from pprint import pprint

import numpy as np
from numpy.lib.stride_tricks import as_strided

persontype = np.dtype(
    {"names": ["name", "age", "weight"], "formats": ["S32", "i", "f"]}, align=True
)


if __name__ == "__main__":
    a = np.array([("Felix", 35, 87.2), ("Tom", 31, 77.4)], dtype=persontype)
    pprint(a)
    pprint(a.dtype)
    pprint(a[0])
    pprint(a[0]["name"])

    c = a[1]
    c["name"] = "Pan"
    pprint(a)

    pprint(a["age"])
    a.tofile("/tmp/a.bin")

    print("\nstruct type can contain other struct type")
    mytype = np.dtype([("f1", [("f2", np.int16)])])
    a = np.array(100, dtype=mytype)
    pprint(a)
    pprint(a["f1"])
    pprint(a["f1"]["f2"])

    print("\ndtype can define shape")
    mytype = np.dtype([("f0", "i4"), ("f1", "f8", (2, 3))])
    pprint(mytype)
    a = np.array(
        [(100, [[1, 2, 3], [4, 5, 6]]), (100, [[7, 7, 7], [6, 6, 6]])], dtype=mytype
    )
    pprint(a)
    pprint(a["f1"])

    print("\nuse dict to define struct type")
    mytype = np.dtype({"surname": ("S25", 0), "age": (np.uint8, 25)})
    pprint(mytype)

    print("\nmemory structure")
    a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float32)
    pprint(a.strides)
    b = a[::2, ::2]
    pprint(b.strides)

    print("\nuse fortran order")
    c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float32, order="F")
    pprint(c.strides)

    print("\nshow flags")
    pprint(c.flags)
    print("\nshow flags of T")
    pprint(c.T.flags)

    print("\nshow base")
    pprint(id(b.base))
    pprint(id(a))

    print("\nas_strided")
    a = np.arange(6)
    b = as_strided(a, shape=(4, 3), strides=(4, 4))
    pprint(b)

    a[2] = 20
    pprint(b)
