import sys
import textwrap


if __name__ == '__main__':
    names = sorted(sys.modules.keys())
    name_text = ', '.join(names)
    print(textwrap.fill(name_text, width=64))
