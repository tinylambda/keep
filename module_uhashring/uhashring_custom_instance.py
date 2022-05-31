import redis
from uhashring import HashRing

# Mapping of dict configs
# Ommited config keys will get a default value, so
# you only need to worry about the ones you need


class MyService:
    def send(self, value):
        print(f"sending value {value}")


nodes = {
    "node1": {
        "hostname": "node1.fqdn",
        "instance": MyService(),
        "port": 6379,
        "vnodes": 40,
        "weight": 1,
    },
    "node2": {
        "hostname": "node2.fqdn",
        "instance": MyService(),
        "port": 6379,
        "vnodes": 40,
    },
    "node3": {"hostname": "node3.fqdn", "instance": MyService(), "port": 6379},
}

# create a new consistent hash ring with the nodes
hr = HashRing(nodes)
hr["coconut0"].send(10)
hr["coconut1"].send(50)
hr["coconut2"].send(100)

print(hr.get_node_port("coconut0"))
