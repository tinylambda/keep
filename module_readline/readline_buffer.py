import readline
import logging


LOG_FILENAME = "/tmp/completer.log"
logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


class BufferAwareCompleter:
    def __init__(self, options):
        self.options = options
        self.current_candidates = []

    def complete(self, text, state):
        # this is the first time **for this text**, so build a match list
        origline = readline.get_line_buffer()
        begin = readline.get_begidx()
        end = readline.get_endidx()
        being_completed = origline[begin:end]
        words = origline.split()

        logging.debug(f"origiline={origline!r}")
        logging.debug(f"begin={begin}")
        logging.debug(f"end={end}")
        logging.debug(f"being_completed={being_completed}")
        logging.debug(f"words={words}")

        if not words:
            self.current_candidates = sorted(self.options.keys())
        else:
            try:
                if begin == 0:
                    # first word
                    candidates = self.options.keys()
                else:
                    # later word
                    first = words[0]
                    candidates = self.options[first]
                if being_completed:
                    # match options with portion of input
                    # being completed
                    self.current_candidates = [
                        w for w in candidates if w.startswith(being_completed)
                    ]
                else:
                    # matching empty string, use all candidates
                    self.current_candidates = candidates
                logging.debug("candidates=%s", self.current_candidates)
            except (KeyError, IndexError) as err:
                logging.error("completion error: %s", err)
                self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug("complete(%s, %s) => %s", repr(text), state, response)
        return response


def input_loop():
    line = ""
    while line != "stop":
        line = input('Prompt ("stop" to quit): ')
        print("Dispatch {}".format(line))


if __name__ == "__main__":
    completer = BufferAwareCompleter(
        {
            "list": ["files", "directories"],
            "print": ["byname", "bysize"],
            "stop": [],
        }
    )
    readline.set_completer(completer.complete)

    # Use the tab key for completion
    readline.parse_and_bind("tab: complete")

    # Prompt the user for text
    input_loop()
