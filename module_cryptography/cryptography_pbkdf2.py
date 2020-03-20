from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256

print(default_backend().pbkdf2_hmac_supported(SHA256()))
print(default_backend().derive_pbkdf2_hmac(SHA256(), 40, b'abcdedfdfd', 10000, b'123'))


