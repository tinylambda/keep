import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class StorageNode:
    name = attr.ib()
    host = attr.ib()

    def put_file(self, path):
        logging.info('[%s -> %s]: putting file %s', self.name, self.host, path)

    def fetch_file(self, path):
        logging.info('[%s -> %s]: fetching file %s', self.name, self.host, path)


storage_nodes = [
        StorageNode(name='A', host='10.131.213.12'),
        StorageNode(name='B', host='10.131.213.11'),
        StorageNode(name='C', host='10.131.213.46'),
        StorageNode(name='D', host='10.131.213.17'),
        StorageNode(name='E', host='10.131.213.18'),
        StorageNode(name='F', host='10.131.213.15'),
        StorageNode(name='G', host='10.131.213.10'),
    ]


def hash_fn(key: str):
    return sum(bytearray(key.encode('utf-8'))) % 7


def upload(path):
    index = hash_fn(path)
    node = storage_nodes[index]
    return node.put_file(path)


def fetch(path):
    index = hash_fn(path)
    node = storage_nodes[index]
    return node.fetch_file(path)


if __name__ == '__main__':
    files = [f'f{i}.txt' for i in range(1, 6)]
    logging.info('%s', ', '.join(files))
    logging.info('%s', files)

    for path in files:
        upload(path)
