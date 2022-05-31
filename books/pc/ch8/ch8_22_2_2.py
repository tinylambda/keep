from books.pc.ch8.ch8_22_2 import NodeVisitor, Number, Add


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


if __name__ == "__main__":
    e = Evaluator()
    a = Number(0)
    for n in range(100000):
        a = Add(a, Number(n))
    print(e.visit(a))
