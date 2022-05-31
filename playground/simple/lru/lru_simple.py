import hashlib
import logging
import sys

import attr

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@attr.s
class Node:
    data = attr.ib()
    next = attr.ib(default=None)
    previous = attr.ib(default=None)


@attr.s
class DLL:
    head = attr.ib(default=None)
    tail = attr.ib(default=None)
    count = attr.ib(default=0)

    def append(self, data):
        if self.head is None:
            self.head = Node(data=data)
            self.tail = self.head
        else:
            self.tail.next = Node(data=data)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        self.count += 1

    def insert(self, data, index):
        if index > self.count or index < 0:
            raise IndexError("out of index")

        if index == self.count:
            self.append(data)
        elif index == 0:
            self.head.previous = Node(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
            self.count += 1
        else:
            start = self.head
            for _ in range(index):
                start = start.next
            start.previous.next = Node(data)
            start.previous.next.previous = start.previous
            start.previous.next.next = start
            start.previous = start.previous.next
            self.count += 1

    def remove(self, index):
        if index >= self.count or index < 0:
            raise IndexError("out of index")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            start = self.head
            for i in range(index):
                start = start.next
            start.previous.next, start.next.previous = start.next, start.previous
        self.count -= 1

    def index(self, data):
        start = self.head
        for i in range(self.count):
            if start.data == data:
                return i
            start = start.next
        return None

    def size(self):
        return self.count

    def display(self):
        print(self)


class LRUCache:
    def __init__(self, max_size):
        self.hm = {}
        self.dll = DLL()
        self.max_size = max_size

    def get(self, key):
        if key not in self.hm:
            logging.info("fetch data for key: %s", key)
            value = self.get_data_from_db(key)
            self.dll.insert(key, 0)
            self.hm[key] = value
        else:
            logging.info("key exists: %s, using cache!", key)

        if self.dll.size() > self.max_size:
            to_be_removed_key = self.dll.tail.data
            logging.info("shrinking key:  %s", to_be_removed_key)
            try:
                del self.hm[to_be_removed_key]
            except KeyError:
                pass
            self.dll.remove(self.dll.size() - 1)

        return self.hm[key]

    @classmethod
    def get_data_from_db(cls, key):
        return hashlib.md5(key.encode()).hexdigest()


if __name__ == "__main__":
    cache = LRUCache(max_size=2)
    print(cache.get("100"))
    print(cache.get("101"))
    print(cache.get("102"))  # remove 100
    print(cache.get("100"))  # remove 101
    print(cache.get("100"))  # nothing happen
