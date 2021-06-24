import gmpy2, os, binascii, string, time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# DO NOT USE - FOR EDUCATIONAL PURPOSES


def simple_rsa_encrypt(m, publickey):
    numbers = publickey.public_numbers()
    return gmpy2.powmod(m, numbers.e, numbers.n)


def simple_rsa_decrypt(c, privatekey):
    numbers = privatekey.private_numbers()
    return gmpy2.powmod(c, numbers.d, numbers.public_numbers.n)


# public exponent (e) indicates what one mathematical property of the key generation will be. Standard practice = 65537
# key size describes how many bits long the key should be (1024 considerable breakable, 2048 >= standard practice)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()
public_mod = public_key.public_numbers().n
message_a = 10
message_b = 15

encrypted_a = simple_rsa_encrypt(message_a, public_key)
encrypted_b = simple_rsa_encrypt(message_b, public_key)

# decrypting the product of two encrypted ciphers == the product of two plaintexts
encrypted_product = (encrypted_a * encrypted_b) % public_mod

decrypted_product = simple_rsa_decrypt(encrypted_product, private_key)

# message_a * message_b = c
# decrypt (encrypted_a * encrypted_b) = c
