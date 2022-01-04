import random

from uhashring import HashRing

if __name__ == '__main__':
    nodes = [f'node_{i}' for i in range(100)]

    for _ in range(100):
        random.shuffle(nodes)
        hr = HashRing(nodes=nodes, hash_fn='ketama')
        target_node = hr.get_node('coconut')
        print(target_node)
