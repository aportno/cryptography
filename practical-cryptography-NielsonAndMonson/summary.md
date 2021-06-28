# ECB
* not collision resistant
### Scenarios
*
# CBC/CTR
* strong
### Scenarios
*

# RSA
* By itself is a deterministic algo opening up risks for reverse engineering (repeated mappings can be saved in a look up table)
* Padding is an essential component to RSA encryption
* Without padding, an encrypted message and be read even without the private key
* PKCS #1 v1.5 padding can be broken with an oracle attack

