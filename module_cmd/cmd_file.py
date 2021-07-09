import cmd


class HelloWorld(cmd.Cmd):
    use_rawinput = False
    prompt = ''

    def do_greet(self, line):
        print('hello', line)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rt') as _input:
        HelloWorld(stdin=_input).cmdloop()

