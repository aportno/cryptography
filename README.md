# Hash Functions
* Message Digest (MD)
* Secure Hash Function (SHA)
* RIPEMD
* Whirlpool
* BLAKE

# Frequency stability property
Coined by Richard von Mises in 1919, the frequency stability property defines an infinite sequence of zeros and ones as not biased (i.e. random) if the frequency of zeroes goes to 1/2 and every subsequence we can select from it by a "proper" method of selection is also not biased.

* 000 should be as frequent as 111, 101, 010, etc
* if the frequency of a subsequence dominates then the generator is not random

# One-way functions
A one-way function is a function that is easy to compute on every input, but hard to invert the given image of a random input

To conceptualize this, imagine Alice and Bob want to communicate to eachother using paint. They are aware that Eve the eavesdropper may be monitoring their communication, and want to ensure Eve does not know what colors each of them have. To start, Alice and Bob and publicly agree on a starting colors, say white and yellow. Next, Alice and Bob randomly select a private color to mix into the public yellow in order to disguise their private color.

* Alice chooses red as her private color and mixes it with the publicly agreed white and yellow producing a pinkish mixture
* Bob chooses blue as his private color and mixes it with the publicly agreed white and yellow producing a green mixture

 Now, Alice sends her mixture to Bob and Bob sends his mixture to Alice. Both assume Eve intercepts these mixtures and is able to see everything exchanged so far. Note that Eve only see's the combined mixture and not the colors Alice and Bob started with.

 Here comes the trick; Alice and Bob now add their own private colors to the mixture they received from one another and arrive at a share secret color:
 
 * Secret color is white and yellow + Alice's red + Bob's blue = some sort of brown mixture
 * Note Eve only knows the mixture sent between the two and not the private colors so she is unable to determine the composition of the mixture.

Numerically, we replace white and yellow starting mixtures with a prime modulus (p) and a generator (g). Alice and Bob agree on these variable publicly, conceding to the fact that Eve is capable of intercepting this transmission. 

* Assume Alice and Bob agree on g = 3, p = 17

Next, Alice and Bob select private random numbers similar to how they selected private colors
* Let Alice choose 15
* Let Bob choose 13

Alice uses modular arithmetic to compute pow(3, 15) mod 17 = 6. She then sends this result (of 6) publicly to Bob. Then Bob perform the same action, using modular arithmetic to compute pow(3, 13) mod 17 = 12, who sends this result publicly to Alice.

Currently:
* Eve knows g = 3, p = 17, and that Alice shared a public number 12, and Bob shared a public number 6. Eve does not know Alice or Bob's private number that generated these numbers

And now the trick; Alice takes Bob's result (of 12) and raises it to the power of her private number and use modular arithmetic to obtain the shared secret. Bob follows the same process using his own private number

* Alice pow(Bob's result = 12, her private number = 15) mod 17 = 10
* Bob pow(Alice's result = 6, his private number = 13) mod 17 = 10


# Algorithms

## Scrypt

## SHA256

## X11

## X13

## X15

## NIST5

## RSA

