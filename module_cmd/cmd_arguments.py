import cmd


class HelloWorld(cmd.Cmd):
    def do_greet(self, person):
        if person:
            print("hi", person)
        else:
            print("hi")

    def do_EOF(self, line):
        return True

    def postloop(self) -> None:
        print()


if __name__ == "__main__":
    HelloWorld().cmdloop()
