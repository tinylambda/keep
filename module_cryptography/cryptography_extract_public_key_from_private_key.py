import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from module_cryptography.cryptography_rsa_generate_private_key import (
    private_key_filename,
)

public_key_filename = "public_key.pem"


if not os.path.exists(public_key_filename):
    with open(private_key_filename, "rb") as private_key_object:
        private_key = serialization.load_pem_private_key(
            private_key_object.read(), password=b"mypassword", backend=default_backend()
        )

    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    print("Write Public key")
    with open(public_key_filename, "wb") as public_key_object:
        public_key_object.write(public_key_pem)
else:
    print("Public key exists")
