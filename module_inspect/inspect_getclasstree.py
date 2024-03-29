import inspect

import module_inspect.example as example


class C(example.B):
    pass


class D(C, example.A):
    pass


def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent + 1)
    else:
        print(" " * indent, tree[0].__name__)


if __name__ == "__main__":
    print("A, B, C, D: ")
    print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))
