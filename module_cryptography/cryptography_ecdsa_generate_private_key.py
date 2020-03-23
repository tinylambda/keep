import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

private_key_filename = 'ecdsa_private_key.pem'


if not os.path.exists(private_key_filename):
    private_key = ec.generate_private_key(
        ec.SECP256K1(),
        default_backend()
    )

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    )

    with open(private_key_filename, 'wb') as f:
        print('Writing PEM File')
        f.write(pem)
else:
    print('private key file exists')


