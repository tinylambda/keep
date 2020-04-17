import array
import binascii
import tempfile


a = array.array('i', range(5))
print('A1: ', a)

# Write the array of numbers to a temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output)
output.flush()

# Read the raw data
with open(output.name, 'rb') as _input:
    raw_data = _input.read()
    print('Raw Contents: ', binascii.hexlify(raw_data))

    # Read the data into an array
    _input.seek(0)
    a2 = array.array('i')
    a2.fromfile(_input, len(a))
    print('A2: ', a2)


