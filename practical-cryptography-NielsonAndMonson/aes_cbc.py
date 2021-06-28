from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(32)
iv = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key),
                   modes.CBC(iv),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
]

ciphertexts = []

for message in plaintexts:
    print(message)
    padded_message = padder.update(message)
    print(padded_message)

    print(ciphertexts)
    ciphertexts.append(aesEncryptor.update(padded_message))
    print(ciphertexts)

ciphertexts.append(aesEncryptor.update(padder.finalize()))

for cipher in ciphertexts:
    padded_message = aesDecryptor.update(cipher)
    print("recovered", unpadder.update(padded_message))

print("recovered", unpadder.finalize())
