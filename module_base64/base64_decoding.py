import base64

if __name__ == '__main__':
    encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
    decoded_data = base64.b64decode(encoded_data)
    print('Encoded: ', encoded_data)
    print('Decoded: ', decoded_data)
