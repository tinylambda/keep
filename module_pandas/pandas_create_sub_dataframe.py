import pandas as pd


account_info = pd.DataFrame({
    'name': ['Bob', 'Mary', 'Mita'],
    'account': [123846, 123972, 347209],
    'balance': [123, 3972, 7209],
})

sub_df = account_info[['name', 'balance']]
print(sub_df)

