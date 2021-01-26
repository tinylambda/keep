import pandas as pd


if __name__ == '__main__':
    s = pd.Series([1, 2, 3, 4, 5, 6])
    s[s % 2 == 0] = 100
    print(s)

    df = pd.DataFrame({
        'x': [1, 2, 3],
        'y': [4, 5, 6]
    })

    print(df)

    for item in df:
        s = df[item]
        s[pd.isna(s)] = 1000

    print(df)

