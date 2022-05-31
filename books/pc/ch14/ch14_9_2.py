def example():
    try:
        int("N/A")
    except ValueError as e:
        raise RuntimeError("a parsing error occurred")


def example2():
    try:
        int("N/A")
    except ValueError as e:
        raise RuntimeError("a parsing error occurred") from e


if __name__ == "__main__":
    # example()
    # example2()

    try:
        example2()
    except RuntimeError as e:
        print("it did not work", e)
        print("..............", e.__cause__)
