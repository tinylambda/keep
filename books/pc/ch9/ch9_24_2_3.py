import ast


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


if __name__ == '__main__':
    code = '''
for i in range(10):
    print(i)
del i
    '''
    top = ast.parse(code, mode='exec')
    c = CodeAnalyzer()
    c.visit(top)
    print('loaded: ', c.loaded)
    print('stored: ', c.stored)
    print('deleted: ', c.deleted)

    exec(compile(top, '<stdin>', 'exec'))

