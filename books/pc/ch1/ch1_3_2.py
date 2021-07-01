from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('/var/log/dmesg') as f:
        for xline, xprevious_lines in search(f, 'input', 5):
            for pline in xprevious_lines:
                print(pline, end='')
            print(xline, end='')
            print('-' * 20)

