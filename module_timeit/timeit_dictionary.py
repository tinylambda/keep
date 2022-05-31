import timeit
import textwrap

range_size = 1000
count = 1000

setup_statement = ";".join(["l = [(str(x), x) for x in range(1000)]", "d = {}"])


def show_results(result):
    """print microseconds per pass and per item."""
    global count, range_size
    per_pass = 1000000 * (result / count)
    print("{:6.2f} usec/pass".format(per_pass), end=" ")
    per_item = per_pass / range_size
    print("{:6.2f} usec/item".format(per_item))


print("{} items".format(range_size))
print("{} iterations".format(count))
print()

print("__setitem__", end=" ")
t = timeit.Timer(
    textwrap.dedent(
        """
    for s, i in l:
        d[s] = i
    """
    ),
    setup_statement,
)
show_results(t.timeit(number=count))


print("setdefault: ", end=" ")
t = timeit.Timer(
    textwrap.dedent(
        """
    for s, i in l:
        d.setdefault(s, i)
    """
    ),
    setup_statement,
)
show_results(t.timeit(number=count))


print("KeyError: ", end=" ")
t = timeit.Timer(
    textwrap.dedent(
        """
    for s, i in l:
        try:
            existing = d[s]
        except KeyError:
            d[s] = i
    """
    ),
    setup_statement,
)
show_results(t.timeit(number=count))

print("not in: ", end=" ")
t = timeit.Timer(
    textwrap.dedent(
        """
    for s, i in l:
        if s not in d:
            d[s] = i
    """
    ),
    setup_statement,
)
show_results(t.timeit(number=count))


"""
python -m timeit -s \
"d={}" \
"for i in range(1000):" \
"    d[str(i)] = i"
1000 loops, best of 5: 212 usec per loop
"""
