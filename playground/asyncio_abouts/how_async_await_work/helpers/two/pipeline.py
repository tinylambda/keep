from follow import follow


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


if __name__ == "__main__":
    with open("/tmp/test.log") as logfile:
        loglines = follow(logfile)
        pylines = grep("python", loglines)

        for line in pylines:
            print(line)
