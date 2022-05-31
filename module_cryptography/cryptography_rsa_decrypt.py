from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

from module_cryptography.cryptography_rsa_generate_private_key import (
    private_key_filename,
)
from module_cryptography.cryptography_rsa_encrypt import cipher_text

with open(private_key_filename, "rb") as private_key_object:
    private_key = serialization.load_pem_private_key(
        private_key_object.read(), password=b"mypassword", backend=default_backend()
    )

plaintext = private_key.decrypt(cipher_text, padding.PKCS1v15())

print(plaintext)
