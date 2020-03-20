from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


from module_cryptography.cryptography_extract_public_key_from_private_key import public_key_filename

message = b'encrypted data'

with open(public_key_filename, 'rb') as public_key_object:
    public_key = serialization.load_pem_public_key(
        data=public_key_object.read(),
        backend=default_backend()
    )

cipher_text = public_key.encrypt(
    message,
    padding.PKCS1v15()
)

print(cipher_text)





