import pandas as pd


if __name__ == '__main__':
    x = pd.Series([1, 2, 3, 4, 5])
    y = pd.Series([2, 3, 4, 5, 6])
    z = x.sub(y, axis=0)
    print(z)

