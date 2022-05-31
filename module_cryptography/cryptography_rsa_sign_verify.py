from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

from module_cryptography.cryptography_rsa_generate_private_key import (
    private_key_filename,
)
from module_cryptography.cryptography_extract_public_key_from_private_key import (
    public_key_filename,
)


message = b"A message I want to sign"

with open(private_key_filename, "rb") as private_key_object:
    private_key = serialization.load_pem_private_key(
        private_key_object.read(), password=b"mypassword", backend=default_backend()
    )

signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

print("Signature: ", signature)

with open(public_key_filename, "rb") as public_key_object:
    public_key = serialization.load_pem_public_key(
        public_key_object.read(), backend=default_backend()
    )

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print("Verify success")
except InvalidSignature:
    print("Verify failed")
