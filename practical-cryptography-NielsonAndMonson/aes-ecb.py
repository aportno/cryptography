# NEVER USE: ECB IS NOT SECURE!

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16) # random 128-bit key
aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()


# First value of each pair is plaintext
# Second value of each pair is ciphertext

nist_kats = [('f34481ec3cc627bacd5dc3fb08f273e6', '0336763e966d92595a567cc9ce537f5e'),
             ('9798c4640bad75c7c3227db910174e72', 'a9a1631bf4996954ebc093957b234589')]

# 16-byte test-private key of all zero's
test_key = bytes.fromhex('00000000000000000000000000000000')

aesCipher2 = Cipher(algorithms.AES(test_key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor2 = aesCipher.encryptor()
aesDecryptor2 = aesCipher.decryptor()

# test-private each input
for index, kat in enumerate(nist_kats):
    plaintext, want_ciphertext = kat
    plaintext_bytes = bytes.fromhex(plaintext)
    ciphertext_bytes = aesEncryptor2.update(plaintext_bytes)
    got_ciphertext = ciphertext_bytes.hex()

    result = "[PASS]" if got_ciphertext == want_ciphertext else "[FAIL]"

    print("Test {}. Expected {}, got {}. Result {}.".format(index, want_ciphertext, got_ciphertext, result))

test_key2 = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key2),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor2 = aesCipher2.encryptor()
aesDecryptor2 = aesCipher2.decryptor()

message = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-01-01

Meet me today at the docks at 2300."""

message += b"E" * (-len(message) % 16)
ciphertext = aesEncryptor.update(message)


