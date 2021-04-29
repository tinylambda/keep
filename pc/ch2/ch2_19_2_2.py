from ch2_19_2 import *


class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._accept('RPAREN')
            return exprval
        else:
            raise SyntaxError('expected NUMBER OR LPAREN')


if __name__ == '__main__':
    e = ExpressionTreeBuilder()
    print(
        e.parse('2 + 3')
    )
    print(
        e.parse('2 + 3 * 4')
    )
    print(e.parse('2 + (3 + 4) * 5'))
    print(e.parse('2 + 3 + 4'))

