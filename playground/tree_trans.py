class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    @classmethod
    def preorder_trans(cls, root):
        res = []
        if root is not None:
            res.append(root.val)
            res = cls.preorder_trans(root.right) + res + cls.preorder_trans(root.left)

        return res


if __name__ == '__main__':
    root = Node(11)
    root.insert(100)
    root.insert(2)
    root.insert(3)
    root.insert(5)
    root.insert(8)

    vals = root.preorder_trans(root)
    print(vals)

