import base64

original_data = b'This is the data, in the clear.'

if __name__ == '__main__':
    print('Original: {} bytes {!r}'.format(len(original_data), original_data))

    b64_data = base64.b64encode(original_data)
    print('b64 Encoded: {} bytes {!r}'.format(len(b64_data), b64_data))

    b85_data = base64.b85encode(original_data)
    print('b85 Encoded: {} bytes {!r}'.format(len(b85_data), b85_data))

    a85_data = base64.a85encode(original_data)
    print('a85 Encode: {} bytes {!r}'.format(len(a85_data), a85_data))
