if __name__ == '__main__':
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits))
    print(fruits)

    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=len, reverse=True))

    fruits.sort()
    print(fruits)

