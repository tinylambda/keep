import base64
import hmac
import hashlib


with open('hmac_sha.py', 'rb') as f:
    body = f.read()

h = hmac.new(
    b'secret-shared-key-goes-here',
    body,
    hashlib.sha1
)

digest = h.digest()
print(base64.encodebytes(digest))

