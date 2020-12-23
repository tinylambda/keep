import pprint
import openpyxl


if __name__ == '__main__':
    xlsx_file = '/Users/Felix/PycharmProjects/document2/配置表/character_rate-统帅养成.xlsx'
    wb = openpyxl.load_workbook(xlsx_file, data_only=True)
    sheet = wb.get_sheet_by_name('character_lv')

    config = []

    i = 0
    for row in sheet:
        i += 1
        if i <= 2:
            continue
        if i == 3:
            headers = [c.value for c in row]
            continue

        values = [c.value for c in row]
        rule_item = dict(zip(headers, values))
        config.append(rule_item)

    # refactor config
    new_config = []
    for rule_item in config:
        new_rule_item = {}
        new_rule_item.update({
            'level': rule_item['level'],
            'quality': 2,
        })
        new_rule_item.update({
            'need_exp': rule_item['normal_need_exp'],
            'extra_add': rule_item['normal_extra_add'],
        })
        new_config.append(new_rule_item)

        new_rule_item = {}
        new_rule_item.update({
            'level': rule_item['level'],
            'quality': 3,
        })
        new_rule_item.update({
            'need_exp': rule_item['rare_need_exp'],
            'extra_add': rule_item['rare_extra_add'],
        })
        new_config.append(new_rule_item)

        new_rule_item = {}
        new_rule_item.update({
            'level': rule_item['level'],
            'quality': 4,
        })
        new_rule_item.update({
            'need_exp': rule_item['epick_need_exp'],
            'extra_add': rule_item['epick_extra_add'],
        })
        new_config.append(new_rule_item)

        new_rule_item = {}
        new_rule_item.update({
            'level': rule_item['level'],
            'quality': 5,
        })
        new_rule_item.update({
            'need_exp': rule_item['legend_need_exp'],
            'extra_add': rule_item['legend_extra_add'],
        })
        new_config.append(new_rule_item)

    pprint.pprint(new_config)
    print(len(new_config))




