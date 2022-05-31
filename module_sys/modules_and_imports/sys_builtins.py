import sys
import textwrap


if __name__ == "__main__":
    name_text = ", ".join(sorted(sys.builtin_module_names))
    print(textwrap.fill(name_text, width=64))
