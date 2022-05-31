from typing import Optional, Tuple

try:
    import gnureadline
    import sys

    sys.modules["readline"] = gnureadline
except ImportError:
    pass

import cmd


class Illustrate(cmd.Cmd):
    def cmdloop(self, intro=None) -> None:
        print(f"cmdloop({intro})")
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self) -> None:
        print("preloop()")

    def postloop(self) -> None:
        print("postloop()")

    def parseline(self, line: str) -> Tuple[Optional[str], Optional[str], str]:
        print(f"parseline({line!r})", end="")
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret

    def onecmd(self, line: str) -> bool:
        print(f"onecmd({line})")
        return cmd.Cmd.onecmd(self, line)

    def emptyline(self) -> bool:
        print("emptyline()")
        return cmd.Cmd.emptyline(self)

    def default(self, line: str) -> bool:
        print(f"default({line})")
        return cmd.Cmd.default(self, line)

    def precmd(self, line: str) -> str:
        print(f"precmd({line})")
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop: bool, line: str) -> bool:
        print(f"postcmd({stop}, {line})")
        return cmd.Cmd.postcmd(self, stop, line)

    def do_greet(self, line):
        print("hello", line)

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    Illustrate().cmdloop()
