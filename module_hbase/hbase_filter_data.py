import happybase

from module_hbase.hbase_insert_data import new_table_name


connection = happybase.Connection('10.1.120.3', port=9090, transport='framed', protocol='compact')
connection.open()

tables = [item.decode() for item in connection.tables()]
assert new_table_name in tables
table = connection.table(new_table_name)

# get data by row key
print(
    table.row('row1')
)
# get data by row key, specify columns
print(
    table.row('row1', columns=['cf1:col1'])
)

print(
    table.row('row1', columns=['cf1:col2'])
)

print(
    table.row('row1', columns=['cf1'])
)

# get rows by keys
print(
    table.rows(['row1', 'row2'])
)

# get rows by keys, specify columns
print(
    table.rows(['row1', 'row2'], columns=['cf1:col1'])
)

print(
    table.rows(['row1', 'row2'], columns=['cf1'])
)

# retrieve multiple versions of a single cell from table
print(
    table.cells('row1', column='cf1:col1', include_timestamp=False)
)

print(
    table.cells('row1', column='cf1:col1', include_timestamp=True)
)


def test_filter(filter=None):
    print('-' * 128, filter)
    for key, data in table.scan(filter=filter):
        print(key, data)


test_filter()
test_filter("PrefixFilter('x')")
test_filter("PageFilter (5)")
test_filter("FirstKeyOnlyFilter ()")
test_filter("KeyOnlyFilter ()")
test_filter("ColumnPrefixFilter ('c')")  # ??????
test_filter("MultipleColumnPrefixFilter ('c')")  # ??????
test_filter("ColumnCountGetFilter (2)")  # ??????
test_filter("InclusiveStopFilter ('x1')")
test_filter("ColumnPaginationFilter (1, 1)")

print('*' * 128)
row_start = '0-100-'
row_stop = '0-100.'
for key, data in table.scan(row_start=row_start, row_stop=row_stop):
    print(key, data)

connection.close()

