if __name__ == "__main__":
    gen = (x.upper() for x in ["hello", "world"])
    print(gen)
    print(list(gen))
