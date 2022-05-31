import ast


if __name__ == "__main__":
    x = 42
    ex = ast.parse("2 + 3 * 4 + x", mode="eval")
    print(ex)
    print(ast.dump(ex))

    top = ast.parse("for i in range(10): print(i)", mode="exec")
    print(top)
    print(ast.dump(top))
