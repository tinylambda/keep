import readline
import logging
import os


LOG_FILENAME = "/tmp/completer.log"
HISTORY_FILENAME = "/tmp/completer.hist"

logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


def get_history_items():
    num_items = readline.get_current_history_length() + 1
    return [readline.get_history_item(i) for i in range(1, num_items)]


class HistoryCompleter:
    def __init__(self):
        self.matches = []

    def complete(self, text, state):
        if state == 0:
            history_values = get_history_items()
            logging.debug("history: %s", history_values)
            if text:
                self.matches = sorted(
                    [h for h in history_values if h and h.startswith(text)]
                )
            else:
                self.matches = []
            logging.debug("matches: %s", self.matches)

        try:
            response = self.matches[state]
        except IndexError:
            response = None

        logging.debug("complete(%s, %s) => %s", repr(text), state, repr(response))
        return response


def input_loop():
    if os.path.exists(HISTORY_FILENAME):
        readline.read_history_file(HISTORY_FILENAME)
    print("Max history file length:", readline.get_current_history_length())
    print("Startup history:", get_history_items())
    try:
        while True:
            line = input('Prompt ("stop" to quit): ')
            if line == "stop":
                break
            if line:
                print("Adding {!r} to the history".format(line))
    finally:
        print("Final history: ", get_history_items())
        readline.write_history_file(HISTORY_FILENAME)


if __name__ == "__main__":
    readline.set_completer(HistoryCompleter().complete)
    readline.parse_and_bind("tab: complete")
    input_loop()
