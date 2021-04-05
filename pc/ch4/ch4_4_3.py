class DepthFirstIterator:
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


class BreadthFirstIterator:
    def __init__(self, start_node):
        self._node = start_node
        self._child_iters = [iter([self._node])]

    def __iter__(self):
        return self

    def __next__(self):
        if self._child_iters:
            try:
                child_iter = self._child_iters[0]
                nextchild = next(child_iter)
                self._child_iters.append(iter(nextchild))
                return nextchild
            except StopIteration:
                self._child_iters.pop(0)
                return self.__next__()
        else:
            raise StopIteration


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)

    def depth_first(self):
        return DepthFirstIterator(self)

    def breadth_first(self):
        return BreadthFirstIterator(self)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    child3 = Node(3)
    child1.add_child(child3)
    child4 = Node(4)
    child1.add_child(child4)
    child5 = Node(5)
    child2.add_child(child5)
    child6 = Node(6)
    child3.add_child(child6)

    for item in root.depth_first():
        print(item)

    print('-' * 64)

    for item in root.breadth_first():
        print(item)

