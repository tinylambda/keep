import base64

encodes_with_pluses = b'\xfb\xef'
encodes_with_slashes = b'\xff\xff'

if __name__ == '__main__':
    for original in [encodes_with_pluses, encodes_with_slashes]:
        print('Original: ', repr(original))
        print('Standard encoding: ', base64.b64encode(original))
        print('URL-safe encoding: ', base64.urlsafe_b64encode(original))
        print()
