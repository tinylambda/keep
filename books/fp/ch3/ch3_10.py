from types import MappingProxyType


if __name__ == "__main__":
    d = {1: "A"}
    d_proxy = MappingProxyType(d)

    print(d_proxy)
    print(d_proxy[1])
    d[2] = "B"
    print(d_proxy)
    print(d_proxy[2])
    d_proxy[3] = "C"
