## ECB
* not collision resistant

## CBC/CTR
* strong

## RSA
Alice and Bob cannot confirm they are communicating with each other given RSAs lack signatures
Eve can intercept the public key sent from Bob, and replace it with their own public key
without Alice knowing. Alice would then be encrypting messages using the Eves public key, allowing
Eve to receive all intended messages. Likewise, Eve could send mis-information to Bob using the
public key initially sent. There is no way for Bob and Alice to confirm they are communicating
each other
