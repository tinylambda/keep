import readline


class SimpleCompleter:
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text
            # so build a match first
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


def input_loop():
    line = ""
    while line != "stop":
        line = input('Prompt ("stop" to quit):')
        print("Dispatch {}".format(line))


OPTIONS = ["start", "stop", "list", "print"]
readline.set_completer(SimpleCompleter(OPTIONS).complete)
readline.parse_and_bind("tab: complete")

input_loop()
