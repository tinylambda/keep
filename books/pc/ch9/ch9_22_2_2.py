from contextlib import contextmanager


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    try:
        yield working
    except Exception as e:
        print(e)
    finally:
        orig_list[:] = working


if __name__ == "__main__":
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)
    print(items)

    with list_transaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("oops")
    print(items)
