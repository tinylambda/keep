from collections import Counter

if __name__ == '__main__':
    words = []
    with open('ch1_1_7_2.py') as f:
        for line in f:
            words.extend(line.split())

    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

    print(
        word_counts['=']
    )

    more_words = []
    with open('ch1_1_8_2.py') as f:
        for line in f:
            more_words.extend(line.split())

    for word in more_words:
        word_counts[word] += 1

    print(word_counts['='])

    word_counts.update(more_words)
    print(word_counts['='])

    a = Counter(words)
    b = Counter(more_words)
    print(a)
    print(b)

    c = a + b
    print(c)

    d = a - b
    print(d['='])
    print(d['gogogogo'])
    print(d.keys())


