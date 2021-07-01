if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(
        sorted(fruits, key=lambda x: x[-1])
    )
    print(
        list(callable(item) for item in [abs, str, '13'])
    )

