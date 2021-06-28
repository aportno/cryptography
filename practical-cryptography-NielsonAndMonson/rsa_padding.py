from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def main():
    message = b'test'

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    ciphertext1 = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    ciphertext2 = public_key.encrypt(
        message,
        padding.PKCS1v15()
    )

    recovered1 = private_key.decrypt(
        ciphertext1,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    recovered2 = private_key.decrypt(
        ciphertext2,
        padding.PKCS1v15()
    )

    print("Plaintext: {}".format(message))
    print("Ciphertext with OAEP padding(hexlified): {}".format(ciphertext1))
    print("Ciphertext with PKCS #1 v1.5 padding(hexlified): {}".format(ciphertext2))
    print("Recovered 1: {}".format(recovered1))
    print("Recovered 2: {}".format(recovered2))


if __name__ == "__main__":
    main()
