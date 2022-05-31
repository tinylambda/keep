import ipaddress


if __name__ == "__main__":
    net = ipaddress.ip_network("123.34.67.64/27")
    print(repr(net))

    for address in net:
        print(address)

    net6 = ipaddress.ip_network("12:3456:78:90ab:cd:ef01:23:30/125")
    print(repr(net6))
    for address in net6:
        print(address)

    print(net.num_addresses)
    print(net6.num_addresses)

    print(repr(net[0]))
    print(repr(net[1]))
    print(repr(net[-1]))
    print(repr(net[-2]))

    a = ipaddress.ip_address("123.34.67.69")
    print(a in net)
    a = ipaddress.ip_address("123.34.67.123")
    print(a in net)

    inet = ipaddress.ip_interface("123.45.67.73/27")
    print(repr(inet.network))
    print(repr(inet.ip))
