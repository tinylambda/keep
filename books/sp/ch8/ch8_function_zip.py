if __name__ == "__main__":
    keys = ["foobar", "barzz", "ba!"]
    lens = map(len, keys)
    print(lens)

    zip_items = zip(keys, lens)
    print(zip_items)
    print(list(zip_items))

    zip_dict = dict(zip(keys, map(len, keys)))
    print(zip_dict)
