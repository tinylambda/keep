def greeting(name):
    return "hello " + name


def greeting_with_type_hint(name: str) -> str:
    return "hello " + name


if __name__ == "__main__":
    greeting(100)
    greeting_with_type_hint(100)


# test with:  mypy module_mypy/mypy_function.py
