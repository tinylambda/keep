import collections


c = collections.Counter('abcdaab')

for letter in 'abcde':
    print(
        '{}: {}'.format(letter, c[letter])
    )  # Counter does not raise KeyError for unknown items


