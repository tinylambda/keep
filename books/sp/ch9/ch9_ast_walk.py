import ast
from _ast import BinOp
from typing import Any


class ReplaceBinOp(ast.NodeTransformer):
    """Replace operation by addition in binary operation"""
    def visit_BinOp(self, node: BinOp) -> Any:
        return ast.BinOp(left=node.left, op=ast.Add(), right=node.right)


if __name__ == '__main__':
    tree = ast.parse('x = 1/3')
    ast.fix_missing_locations(tree)
    eval(compile(tree, '', 'exec'))
    print(ast.dump(tree))
    print(x)

    tree = ReplaceBinOp().visit(tree)
    ast.fix_missing_locations(tree)
    print(ast.dump(tree))
    eval(compile(tree, '', 'exec'))
    print(x)


