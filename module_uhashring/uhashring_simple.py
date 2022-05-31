from uhashring import HashRing

# create a consistent hash ring of 3 nodes of weight 1
hr = HashRing(nodes=["node1", "node2", "node3"])

# get the node name for the 'coconut' key
target_node = hr.get_node("coconut")
