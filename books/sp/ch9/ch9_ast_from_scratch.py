import ast


if __name__ == '__main__':
    hello_world = ast.Str(s='hello world!', lineno=1, col_offset=1)
    print_name = ast.Name(id='print', ctx=ast.Load(), lineno=1, col_offset=1)
    print_call = ast.Call(func=print_name, ctx=ast.Load(), args=[hello_world], keywords=[], lineno=1, col_offset=1)
    module = ast.Module(
        [ast.Expr(print_call, lineno=1, col_offset=1)],
        [],
    )
    code = compile(module, '<input>', 'exec')
    eval(code)

