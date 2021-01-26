import pandas as pd
import types, typing
import inspect


if __name__ == '__main__':
    excel_file = '/home/felix/PycharmProjects/document/配置表/character_detail-统帅基础.xlsx'
    df = pd.read_excel(excel_file, sheet_name='character_detail', engine='openpyxl')

    cn_name_series = df.columns.to_series()
    type_name_series = df.iloc[0]
    en_name_series = df.iloc[1]

    r = pd.isna(en_name_series)
    print(r)
    en_name_series[r] = cn_name_series[r]

    new_data = {}
    for item in df:
        s = df[item]
        cn_name = item
        type_name = s[0]
        en_name = s[1] or cn_name

        v = str
        default = ''
        if pd.isna(type_name):
            v = str
        elif isinstance(type_name, str) and type_name:
            if type_name.endswith('int'):
                v = int
                default = 0
            elif type_name == 'float':
                v = float,
                default = 0.0
        else:
            print(cn_name, en_name, type_name, 'Cannot be processed')

        s[pd.isna(s)] = default
        s = s[2:]
        try:
            s = s.astype(v)
        except Exception as e:
            pass
        else:
            new_data.update({en_name: s})

    df = pd.DataFrame(new_data)


