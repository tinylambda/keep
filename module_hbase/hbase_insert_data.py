import happybase


connection = happybase.Connection('10.1.120.3', port=9090, transport='framed', protocol='compact')
connection.open()

new_table_name = 'testtable'
tables = [item.decode() for item in connection.tables()]

if new_table_name not in tables:
    connection.create_table(
        new_table_name, {
            'cf1': {
                'max_versions': 10,
            }
        }
    )

new_table = connection.table(new_table_name)
new_table.put(b'row1', {
    b'cf1:col1': b'value1',
    b'cf1:col2': b'value2',
})
new_table.put(b'row2', {
    b'cf1:col1': b'value3',
    b'cf1:col2': b'value4',
})
new_table.put(b'x1', {
    b'cf1:col1': b'value3',
    b'cf1:col2': b'value4',
})
new_table.put(b'x2', {
    b'cf1:col1': b'value3',
    b'cf1:col2': b'value4',
})
new_table.put(b'y1', {
    b'cf1:col8': b'value3',
    b'cf1:col9': b'value4',
})
new_table.put(b'y2', {
    b'cf1:col7': b'value3',
    b'cf1:col6': b'value4',
    b'cf1:col5': b'value5',
})

new_table.put(b'98', {
    b'cf1:col7': b'value3',
})
new_table.put(b'99', {
    b'cf1:col7': b'value3',
})
new_table.put(b'100', {
    b'cf1:col7': b'value3',
})
new_table.put(b'101', {
    b'cf1:col7': b'value3',
})
new_table.put(b'198', {
    b'cf1:col7': b'value3',
})


new_table.put(b'0-100-2-xx', {
    b'cf1:col7': b'value3',
})
new_table.put(b'0-100-2-yy', {
    b'cf1:col7': b'value3',
})
new_table.put(b'0-1000-2-yy', {
    b'cf1:col7': b'value3',
})
new_table.put(b'0-120-2-zz', {
    b'cf1:col7': b'value3',
})
new_table.put(b'0-130-2-mm', {
    b'cf1:col7': b'value3',
})

new_table.put(b'num-1', {
    b'cf1:col1': int.to_bytes(100),
})
new_table.put(b'num-2', {
    b'cf1:col1': int.to_bytes(10),
})
new_table.put(b'num-3', {
})
connection.close()
