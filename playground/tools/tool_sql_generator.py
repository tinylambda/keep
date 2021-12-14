import datetime

records = '''196947	104097454	0	4
276575	104633386	0	4
369387	105149555	0	4
372117	105190152	0	4
466943	107564331	0	8
478409	108050359	0	4
1693	105834088	0	8'''
record_head = ['operation_id', 'orientation_id', 'operation_type', 'match_type']
record_list = records.split('\n')
record_dict_list = [dict(zip(record_head, item.split())) for item in record_list]

table_operation = {
    'id_column': 'id_string',
}

table_user_full = {
    'mobile_md5_column': 'phone_md5',
    'mobile_sha256_column': 'phone_sha256',
}

table_user_active = {
    'mobile_md5_column': 'phone_md5',
    'mobile_sha256_column': 'phone_sha256',
}

sql_template = '''
select
X0.orientation_id,
X1.upload_count,
X1.upload_count_distinct,
X0.full_cover_num,
X0.mau_cover_num
from
(select 
'{orientation_id}' as orientation_id,
count(distinct T1.user_id) as full_cover_num,
count(distinct T2.user_id) as mau_cover_num
from
(select id_string as id_string
from operation_table
where operation_id='{operation_id}') T0
left outer join
(select 
{full_match_column} as full_match_column,
user_id as user_id
from full_table
where p_date='{p_date}') T1
on T0.id_string = T1.full_match_column
left outer join
(select 
{active_match_column} as active_match_column,
user_id as user_id
from mau_table
where p_date='{p_date}') T2
on T0.id_string = T2.active_match_column) X0
left outer join
(select 
'{orientation_id}' as orientation_id,
count(id_string) as upload_count,
count(distinct id_string) as upload_count_distinct
from operation_table
where operation_id='{operation_id}') X1
on X0.orientation_id = X1.orientation_id
'''


if __name__ == '__main__':
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    p_date = yesterday.strftime('%Y%m%d')

    sql_list = []
    for record_dict in record_dict_list:
        context = {}
        context.update(record_dict)

        match_type = record_dict.get('match_type')
        if match_type == '4':
            full_match_column = table_user_full.get('mobile_md5_column')
            active_match_column = table_user_active.get('mobile_md5_column')
        elif match_type == '8':
            full_match_column = table_user_full.get('mobile_sha256_column')
            active_match_column = table_user_active.get('mobile_sha256_column')
        else:
            raise ValueError(f'match_type should be 4 or 8, but got {match_type}')
        context.update(full_match_column=full_match_column, active_match_column=active_match_column)
        context.update(p_date=p_date)
        sql_list.append(sql_template.format(**context))

    full_sql = 'UNION'.join(sql_list)
    print(full_sql)


