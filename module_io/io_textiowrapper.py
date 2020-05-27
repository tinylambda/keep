import io


# Writing to a buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
wrapper.write('This goes into the buffer.')
wrapper.write('中国地图')

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory

# Initialize a read buffer
input = io.BytesIO(
    b'Initial value for read buffer with unicode characters ' + '中国地图'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Read from the buffer
print(wrapper.read())

