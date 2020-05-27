import io


# Writing to a buffer
output = io.BytesIO()
output.write('This goes into the buffer.'.encode('utf-8'))
output.write('中国地图'.encode('utf-8'))

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory


# Initialize a read buffer
input = io.BytesIO(b'Initial value for read buffer')

# Read from the buffer
print(input.read())

