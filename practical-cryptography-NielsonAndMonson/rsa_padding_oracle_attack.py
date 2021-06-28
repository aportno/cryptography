from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from rsa_sample import simple_rsa_encrypt, simple_rsa_decrypt, bytes_to_int, int_to_bytes
from rsa_key_generation import private_key, public_key

import gmpy2

from collections import namedtuple

Interval = namedtuple('Interval', ['a', 'b'])

message = b'test'

# WARNING: PKCS #1 v1.5 is obsolete and has vulnerabilities

ciphertext = public_key.encrypt(
    message,
    padding.PKCS1v15()
)

ciphertext_as_int = bytes_to_int(ciphertext)


class FakeOracle:
    def __init__(self, private_key):
        self.private_key = private_key

    def __call__(self, cipher_text):
        recovered_as_int = simple_rsa_decrypt(cipher_text, self.private_key)
        recovered = int_to_bytes(recovered_as_int, self.private_key.key_size // 8)
        return recovered[0:2] == bytes([0, 2])


class RSAOracleAttacker:
    def __init__(self, public_key, oracle):
        self.public_key = public_key
        self.oracle = oracle

    def _step1_blinding(self, c):
        self.c0 = c

        self.B = 2 ** (self.public_key.key_size - 16)
        self.s = [1]
        self.M = [[Interval(2 * self.B, (3 * self.B) - 1)]]

        self.i = 1
        self.n = self.public_key.public_numbers().n

    def _find_s(self, start_s, s_max = None):
        si = start_s
        ci = simple_rsa_encrypt(si, self.public_key)

        while not self.oracle((self.c0 * ci) % self.n):
            si += 1
            if s_max and (si > s_max):
                return None
            ci = simple_rsa_encrypt(si, self.public_key)
        return si

    def _step2a_start_the_search(self):
        si = self._find_s(start_s=gmpy2.c_div(self.n, 3*self.B))
        return si
