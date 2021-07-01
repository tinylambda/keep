from books.fp.ch14.ch14_1 import Sentence


if __name__ == '__main__':
    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(
        it
    )

    print(next(it))
    print(next(it))
    print(next(it))

    try:
        print(next(it))
    except StopIteration:
        print('StopIteration')

    print(list(it))
    print(list(s3))

