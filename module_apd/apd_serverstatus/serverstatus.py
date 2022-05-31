import sys
import socket
import psutil


def python_version():
    return sys.version_info


def ip_address():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)
    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info


def cpu_load():
    return psutil.cpu_percent()


def ram_available():
    return psutil.virtual_memory().available


def ac_connected():
    return psutil.sensors_battery().power_plugged


if __name__ == "__main__":
    print(ip_address())
