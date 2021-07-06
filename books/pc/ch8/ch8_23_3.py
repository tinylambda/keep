class Data:
    def __del__(self):
        print('Data.__del__')


class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    a = Data()
    del a

    a = Node()
    del a

    a = Node()
    a.add_child(Node())
    del a

