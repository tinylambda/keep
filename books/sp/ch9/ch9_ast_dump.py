import ast


if __name__ == '__main__':
    print(ast.parse)
    parse_result = ast.parse('x = 87')
    print(parse_result)

    dump_result = ast.dump(parse_result)
    print(dump_result)

    compile(ast.parse('x = 42'), '<input>', 'exec')

    eval(compile(ast.parse('x = 87'), '<input>', 'exec'))
    print(x)

