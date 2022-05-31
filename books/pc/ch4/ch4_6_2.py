from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == "__main__":
    with open("/etc/passwd") as f:
        lines = LineHistory(f)
        for line in lines:
            if "root" in line:
                print("got one")
                for lineno, hline in lines.history:
                    print("{}:{}".format(lineno, hline), end="")
