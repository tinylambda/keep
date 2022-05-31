import sys
import traceback


def sample(n):
    if n > 0:
        sample(n - 1)
    else:
        traceback.print_stack(file=sys.stderr)


if __name__ == "__main__":
    sample(3)
