if __name__ == "__main__":
    filter_items = filter(lambda x: x.startswith("I "), ["I think", "I'm good"])
    print(filter_items)
    print(list(filter_items))

    filter_items = (x for x in ["I think", "I'm good"] if x.startswith("I "))
    print(filter_items)
    print(list(filter_items))
