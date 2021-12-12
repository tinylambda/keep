from pprint import pprint


class Node:
    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return f'Node({repr(self.name)}, {repr(self.contents)})'


if __name__ == '__main__':
    trees = [
        Node('node-1'),
        Node('node-2', [Node('node-2-1')]),
        Node('node-3', [Node('node-3-1')])
    ]
    pprint(trees)
