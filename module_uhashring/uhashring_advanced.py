import redis
from uhashring import HashRing

# Mapping of dict configs
# Ommited config keys will get a default value, so
# you only need to worry about the ones you need
nodes = {
    "node1": {
        "hostname": "node1.fqdn",
        "instance": redis.StrictRedis(host="node1.fqdn"),
        "port": 6379,
        "vnodes": 40,
        "weight": 1,
    },
    "node2": {
        "hostname": "node2.fqdn",
        "instance": redis.StrictRedis(host="node2.fqdn"),
        "port": 6379,
        "vnodes": 40,
    },
    "node3": {
        "hostname": "node3.fqdn",
        "instance": redis.StrictRedis(host="node3.fqdn"),
        "port": 6379,
    },
}

# create a new consistent hash ring with the nodes
hr = HashRing(nodes)
print(hr["coconut0"])
print(hr["coconut1"])
print(hr["coconut2"])

print(hr.get_server("coconut0"))
print(hr.get_server("coconut1"))
print(hr.get_server("coconut2"))


print(hr.get_node_port("coconut0"))


# # set the 'coconut' key/value on the right host's redis instance
# hr['coconut'].set('coconut', 'my_value')
#
# # get the 'coconut' key from the right host's redis instance
# hr['coconut'].get('coconut')
#
# # delete the 'coconut' key on the right host's redis instance
# hr['coconut'].delete('coconut')
#
# # get the node config for the 'coconut' key
# conf = hr.get('coconut')
