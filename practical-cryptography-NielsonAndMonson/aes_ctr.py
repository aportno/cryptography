from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


class EncryptionManager:
    def __init__(self):
        key = os.urandom(32)
        nonce = os.urandom(16)
        aes_context = Cipher(algorithms.AES(key),
                             modes.CTR(nonce),
                             backend=default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()

    def updateEncryptor(self, plaintext):
        return self.encryptor.update(plaintext)

    def finalizeEncryptor(self):
        return self.encryptor.finalize()

    def updateDecryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)

    def finalizeDecryptor(self):
        return self.decryptor.finalize()


manager = EncryptionManager()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
]

ciphertexts = []

for message in plaintexts:
    ciphertexts.append(manager.updateEncryptor(message))
ciphertexts.append(manager.finalizeEncryptor())

for cipher in ciphertexts:
    print("Recovered", manager.updateDecryptor(cipher))
print("Recovered", manager.finalizeDecryptor())
