from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class Oracle:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def accept(self, ciphertext):
        aesCipher = Cipher(algorithms.AES(key),
                           modes.CBC(iv),
                           backend=default_backend())
        decryptor = aesCipher.decryptor()
        plaintext = decryptor.update(ciphertext)
        plaintext += decryptor.finalize()
        return plaintext[-1] == 15


def lucky_get_one_byte(iv, ciphertext, block_number, oracle):
    block_start = block_number * 16
    block_end = block_start + 16
    block = ciphertext[block_start:block_end]

    mod_ciphertext = ciphertext[:-16] + block
    if not oracle.accept(mod_ciphertext):
        return False, None

    second_to_last = ciphertext[-32:-16]
    intermediate = second_to_last[-1]^15

    if block_number == 0:
        prev_block = iv
    else:
        prev_block = ciphertext[block_start-16:block_start]

    return True, intermediate ^ prev_block[-1]
