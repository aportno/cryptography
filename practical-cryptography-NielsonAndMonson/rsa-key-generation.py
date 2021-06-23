from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# public key derived from private key
public_key = private_key.public_key()

# convert private key into bytes
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# convert public key into bytes
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# convert private key bytes back to a key
private_key = serialization.load_pem_private_key(
    private_key_bytes,
    backend=default_backend(),
    password=None
)

public_key = serialization.load_pem_public_key(
    public_key_bytes,
    backend=default_backend()
)
