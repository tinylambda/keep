# use procedure programming
s = 0
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n
print(s)

# use oop
m = []
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)
print(sum(m))


# use strict oop
class SummableList(list):
    def sum(self):
        s = 0
        for v in self:
            s += v
        return s


m = SummableList()
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)
print(m.sum())


# recursive
def sumr(seq):
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + sumr(seq[1:])


print(sumr([7, 11]))


# more abstract
def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n, filter_func, v+1)


multi_3_5 = lambda x: x % 3 == 0 or x % 5 == 0

multi_3_5_nums = until(10, multi_3_5, 0)
print(multi_3_5_nums, sum(multi_3_5_nums))


# mix style
print(sum(n for n in range(1, 10) if n % 3 ==0 or n % 5 == 0))


# functional classic example
def next_(n, x):
    return (x + n / x) / 2

n = 2
f = lambda x: next_(n, x)
a0 = 1.0
result = [round(x, 4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))),)]
print(result)


def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v


def within(e, iterable):
    def head_tail(e, a, iterable):
        b = next(iterable)
        if abs(a-b) < e:
            return b
        else:
            return head_tail(e, b, iterable)
    return head_tail(e, next(iterable), iterable)


def sqrt(a0, e, n):
    return within(e, repeat(lambda x: next_(n, x), a0))


result = sqrt(1.0, 0.0001, 3)
print(result)


