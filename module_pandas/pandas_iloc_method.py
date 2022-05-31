import pandas as pd


account_info = pd.DataFrame(
    {
        "name": ["Bob", "Mary", "Mita"],
        "account": [123846, 123972, 347209],
        "balance": [123, 3972, 7209],
    }
)

print("Original: ", account_info)
print()
print("iloc[1]: \n", account_info.iloc[1])
print()
print("iloc[0:2]: \n", account_info.iloc[0:2])
print()
print("iloc[:]\n", account_info.iloc[:])
