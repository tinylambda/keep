import pandas
import pprint


if __name__ == '__main__':
    excel_file = '/home/felix/PycharmProjects/document/配置表/character_rate-统帅养成.xlsx'
    df = pandas.read_excel(excel_file, sheet_name='character_star', engine='openpyxl', skiprows=2)
    print(df.iloc[0])
    # x = df.loc[:, 'normal_extra_add'][1]
    # print(eval(x))
    # pprint.pprint(df.to_dict(orient='records'))

    for item in df:
        print(df[item])
        print('-' * 64)

