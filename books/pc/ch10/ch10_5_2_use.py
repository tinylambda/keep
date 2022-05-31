import sys


if __name__ == "__main__":
    sys.path.extend(["ch10_5_2_dirs/foo-package", "ch10_5_2_dirs/bar-package"])

    import spam.blah
    import spam.grok

    import spam

    print(spam.__path__)

    sys.path.append("ch10_5_2_dirs/my-package")
    import spam.custom

    print(spam.__file__)
    print(spam)
