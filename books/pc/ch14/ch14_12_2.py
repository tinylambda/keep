def func(n):
    return n + 10


if __name__ == '__main__':
    func('hello')


# (venv) [felix@localhost keep]$ python -i books/pc/ch14/ch14_12_2.py
# Traceback (most recent call last):
#   File "/home/felix/PycharmProjects/keep/books/pc/ch14/ch14_12_2.py", line 5, in <module>
#     func('hello')
#   File "/home/felix/PycharmProjects/keep/books/pc/ch14/ch14_12_2.py", line 2, in func
#     return n + 10
# TypeError: can only concatenate str (not "int") to str
# >>> func(10)
# 20
# >>>
