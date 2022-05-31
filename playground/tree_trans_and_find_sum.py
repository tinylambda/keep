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
    def inorder_trans(cls, root, s=0):
        res = []
        if root is not None:
            res = cls.inorder_trans(root.left, s)
            res.append(root.val)
            if sum(res) == s:
                print("Got!", res)
                return res
            res = res + cls.inorder_trans(root.right, s)
        return res

    @classmethod
    def preorder_trans(cls, root, s=0):
        res = []
        if root is not None:
            res.append(root.val)
            if sum(res) == s:
                print("Got!", res)
                return res
            res = (
                res
                + cls.preorder_trans(root.left, s)
                + cls.preorder_trans(root.right, s)
            )
        return res

    @classmethod
    def postorder_trans(cls, root, s=0):
        res = []
        if root is not None:
            res = cls.postorder_trans(root.left, s)
            res = res + cls.postorder_trans(root.right, s)
            res.append(root.val)
            if sum(res) == s:
                print("Got!", res)
                return res
        return res


if __name__ == "__main__":
    root = Node(11)
    root.insert(100)
    root.insert(2)
    root.insert(3)
    root.insert(5)
    root.insert(8)

    vals = root.inorder_trans(root, s=16)
    print(vals)
    print("-" * 100)

    vals = root.preorder_trans(root, s=16)
    print(vals)
    print("-" * 100)

    vals = root.postorder_trans(root, s=16)
    print(vals)
    print("-" * 100)
