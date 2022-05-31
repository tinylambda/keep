import readline


readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

if __name__ == "__main__":
    while True:
        line = input('Prompt ("stop" to quit):')
        if line == "stop":
            break
        print("Entered: {!r}".format(line))
