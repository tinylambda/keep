import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    number_types_set = {'int', 'bigint', 'float', 'double', 'smallint', 'long'}
    string_types_set = {'string'}

    tables: dict = yaml.safe_load(open('tables.yaml'))

    for table_name, table_detail in tables.items():
        logging.info('Table: %s', table_name)
        for column in table_detail['columns']:
            logging.info('\t\t%s', column)

    datasets: dict = yaml.safe_load(open('datasets.yaml'))
    for dataset_name, dataset in datasets.items():
        logging.info('%s', dataset_name)
        logging.info('\t\t%s', dataset)

    task_context = dict(biz_id=100000101, match_type='IMEI', operation_id=11023)
    # user_upload_dataset intersect
    dataset_upload: dict = datasets.get('user_upload_dataset')
    imei_mapping_dataset: dict = datasets.get('imei_mapping_dataset')
    logging.info('%s', dataset_upload)
    logging.info('%s', imei_mapping_dataset)

    # construct first input
    parts_one = {}
    table_name = dataset_upload.get('base_table')
    assert table_name in tables
    key_column_name = dataset_upload.get('key_column')
    table = tables.get(table_name)
    assert any(item['name'] == key_column_name for item in table.get('columns', []))
    logging.info('%s', table)
    select_items = [item['name'] for item in table.get('columns', [])]
    logging.info('select items: %s', select_items)

    read_filter = dataset_upload.get('read_filter', [])  # a list of list of dict

    if read_filter:
        for group in read_filter:
            ops = [item['op'] for item in group]
            names = [item['name'] for item in group]
            values = [
                f'{task_context[name]}' if name in number_types_set else f'\'{task_context[name]}\''
                for name in names]
            conds = [' '.join(item) for item in zip(names, ops, values)]
            conds_string = ' and '.join(conds)
            logging.info('%s', conds_string)





