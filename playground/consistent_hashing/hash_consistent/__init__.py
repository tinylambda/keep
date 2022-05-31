import bisect
import hashlib
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class StorageNode:
    name = attr.ib()
    host = attr.ib()

    def fetch_file(self, path):
        logging.info("[%s - %s]: fetching file: %s", self.name, self.host, path)

    def put_file(self, path):
        logging.info("[%s - %s]: putting file: %s", self.name, self.host, path)


# storage_nodes holding instances of actual storage node objects
storage_nodes = [
    StorageNode(name="A", host="239.67.52.72"),
    StorageNode(name="B", host="137.70.131.229"),
    StorageNode(name="C", host="98.5.87.182"),
    StorageNode(name="D", host="11.225.158.95"),
    StorageNode(name="E", host="203.187.116.210"),
]


def hash_fn(key: str):
    return sum(bytearray(key.encode("utf-8"))) % 5


def upload(path):
    index = hash_fn(path)
    node = storage_nodes[index]
    return node.put_file(path)


def fetch(path):
    index = hash_fn(path)
    node = storage_nodes[index]
    return node.fetch_file(path)


files = [f"f{item}" for item in range(1, 6)]
for file in files:
    logging.info("file %s resides on node %s", file, storage_nodes[hash_fn(file)].name)


logging.info("scale up...")

# storage_nodes holding instances of actual storage node objects
storage_nodes = [
    StorageNode(name="A", host="239.67.52.72"),
    StorageNode(name="B", host="137.70.131.229"),
    StorageNode(name="C", host="98.5.87.182"),
    StorageNode(name="D", host="11.225.158.95"),
    StorageNode(name="E", host="203.187.116.210"),
    StorageNode(name="F", host="107.117.238.203"),
    StorageNode(name="G", host="27.161.219.131"),
]


def hash_fn(key: str):
    return sum(bytearray(key.encode("utf-8"))) % 7


for file in files:
    logging.info("file %s resides on node %s", file, storage_nodes[hash_fn(file)].name)


logging.info("consistent hash")


def hash_fn(key: str, total_slots: int) -> int:
    hasher = hashlib.sha256()
    hasher.update(key.encode("utf-8"))
    return int(hasher.hexdigest(), 16) % total_slots


@attr.s
class ConsistentHash:
    keys = attr.ib(type=list, default=attr.Factory(list))
    nodes = attr.ib(type=list, default=attr.Factory(list))
    total_slots = attr.ib(type=int, default=50)

    def add_node(self, node: StorageNode) -> int:
        if len(self.keys) == self.total_slots:
            raise RuntimeError("hash space full")

        key = hash_fn(node.host, self.total_slots)
        # find the index where the key should be inserted in the keys array
        # this will be the index where the Storage Node will be added in the nodes array
        index = bisect.bisect(self.keys, key)

        logging.info("add to index %s", index)
        # if we have already seen the key i.e. node already is present for the same key, raise collision exception
        if index > 0 and self.keys[index - 1] == key:
            raise RuntimeError("collision occurred")

        # insert the node_id and the key at the same `index` location
        # this insertion will keep nodes and keys sorted w.r.t keys.
        self.nodes.insert(index, node)
        self.keys.insert(index, key)

        return key

    def remove_node(self, node: StorageNode) -> int:
        if len(self.keys) == 0:
            raise RuntimeError("hash space is empty")

        key = hash_fn(node.host, self.total_slots)
        index = bisect.bisect_left(self.keys, key)
        if index >= len(self.keys) or self.keys[index] != key:
            raise RuntimeError("node does not exist")

        self.keys.pop(index)
        self.nodes.pop(index)

        return key

    def assign(self, item: str) -> str:
        key = hash_fn(item, self.total_slots)
        index = bisect.bisect_right(self.keys, key) % len(self.keys)
        return self.nodes[index]


if __name__ == "__main__":
    consistent_hash = ConsistentHash(total_slots=10000)
    consistent_hash.add_node(StorageNode("A1", "111.111.111.111"))
    consistent_hash.add_node(StorageNode("A2", "111.111.111.112"))
    consistent_hash.add_node(StorageNode("A3", "111.111.111.113"))
    consistent_hash.add_node(StorageNode("B1", "111.111.111.114"))
    consistent_hash.add_node(StorageNode("B2", "111.111.111.115"))
    consistent_hash.add_node(StorageNode("B3", "111.111.111.116"))

    for i in range(100):
        logging.info("%s", consistent_hash.assign(f"x{i}"))
