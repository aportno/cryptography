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

## Diffie-hellman key exchange
---

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

Intuition:

Alice generates a private key by randomly selecting a color, say red. Then assume Alice can use some "color machine" to find the complement of her red and no body else has access to this. The results in cyan which sends to Bob as her public key. Remember, at all times we assume Eve intercepts all communication between Alice and Bob.

Now assume Bob wants to send a secret yellow to Alice. He can mix this with her public key (cyan) and then send the mixture back to her. At this point:

* Alice has her private key (red), the public key (cyan) and Bob's secret mixture (of cyan + yellow)
* Bob has the public key (cyan), his secret message (yellow) and the secret mixture (cyan + yellow)
* Eve has the public key (cyan) and the secret mixture (cyan + yellow)

If Alice adds her private color (red) to Bob's secret mixture (cyan + yellow) then the effect of her public color (cyan) is undone leaving her with Bob's secret color (yellow). Eve has no easy way to find Bob's yellow because she needs private red to do so.

Technical:

The British mathematician and cryptographer, Clifford Cocks, found the numerical solution to the problem. He realized he needed to construct a special kind of one-way function called a **trap door one way function**.

The trap door one way function is:
* Easy to compute in one direction
* Hard to compute in the opposite direction (reverse) UNLESS you have special information called the trap door

To achieve this, he turned to modular exponentiation. This can be used to encrypt a message as follows:

* Imagine Bob has a message that is converted into a number, m
* He then multiplies the number by itself _e_ times, where _e_ is a public exponent
* Then Bob divides the result by a random number, _N_
* And finally outputs the remainder of the division, resulting in some number, _c_

The arithmetic is easy to compute, but very challenging to reverse engineer to solve for _m_ if only _c_, _N_, and _e_ are known. That is, it is very challenging to decrypt the ciphertext without knowing the plaintext

So how would you go about decrypting the message? We'd need to raise _c_ to some exponent, _d_, and then use the same modular arithmetic using _N_. We can think of this as:
* If _m_ raised to _e_ mod _N_ equals _c_
* and _c_ raised to _d_ mod _N_ equals _m_
* then we can substitute _c_ for _m_ raised to _e_ resulting in:
* _m_ raised to _e_ raised to _d_ mod _N_ equals _m_; the decrypted message!
* We can simplify this to _m_ raised to (_e_ * _d_) mod _N_ equals m

This means Alice needs to find a way to construct _e_ and _d_ which makes it difficult for anyone else to find _d_. Cocks realized a second one way function could be used to generate _d_. He used Euclid as his inspiration

Over 1,000 years ago, Euclid showed every number has exactly one prime factorization, which we can think of as a secret key. Prime factorization is fundamentally a very challenging problem. We can clarify this difficulty, "easy" verse "hard", by introducing **time complexity**

The time spent for a computer to multiply two numbers increases as the size of the two numbers increase in a ~linear fashion. This is a relatively easy task for the computer as it takes seconds to perform large computations

Compare this to prime factorization, where brute force or trial and error is required to find a number that evenly divides into a given number, say 589. After multiple iterations, you will run into two numbers which multiplied together equal 589, namely 19 times 31. But what if you were asked to find the prime factorization of a very, very large number like 437,231? You'd probably give-up the short-hand trial and error and turn to a computer to compute the result

Finding the prime factors of small numbers is trivial for the computer, so the time to compute is short, or "easy". But as the number because larger, say with 20 digits, the time to compute is non-linear and rapidly increases from seconds to years. Yes, **YEARS** for the computer to find the prime factors. The growth rate of the time needed to solve allows us to define the problem as "hard"

Cocks used prime factorization as the mechanism to build the **trap door solution**:
1. Imagine Alice generates a random number over 150 digits long. We will call this number _P1_
2. Then generates a second random number roughly the same size, we will call this number _P2_
3. She then multiplies _P1_ * _P2_ to get a composite number _N_, which is over 300 digits long

Alice could share this number _N_ publicly as it would take years to find the solution for _P1_ and _P2_. Cocks saw that he needed to find a function that depends on knowing the factorization of _N_. For this, he looked back to the work done by Swiss mathematician, Leonhard Euler in 1760.

Euler discovered and defined the **phi function**, which measures the "breakability" of a number. So given a number, say _N_, it outputs how many integers are less than or equal to _N_ that do not share any common factor with _N_.

For example, if we want to find the **phi** of 8:
1. We look at all values from 1 to 8
2. Then we count all integers from 1 to 8 that 8 does not share a factor greater than one with
3. this would result in 1, 3, 5, and 7. **Notice** 2 is not counted because 2 is a factor of 8; 6 is not counted because 2 is a factor of 6, and also a factor of 8. Likewise, 1, 3, 5, and 7 are counted because the only factor they share with 8 is 1.
4. Therefore, **phi** of 8 equals 4 (the length of the result, i.e., 1, 3, 5, 7)

Finding the **phi** of a number is not trivial, but since prime numbers have no factors greater than 1, the **phi** of any number, _p_ is simply _p_ - 1. This is much easier to compute

Example:
* What is **phi** of 7?
    * 7 = _p_
    * p - 1 = 6, that is there are 6 numbers that do not share a common factor with 7
        * 1, 2, 3, 4, 5, 6 = 6 numbers
* What is **phi** of 21,377?
    * This is a prime number so it equals 21,377 - 1 = 21,376

This leads to an interesting fact that the **phi function** is also multiplicative:
* **phi** A * B = **phi** A * **phi** B 

And if we know that _N_ was the product of two prime numbers _P1_ and _P2_, then:
* **phi** N = **phi** _P1_ * **phi** _P2_

Lastly, we know **phi** of a prime is equal to prime - 1, thus:
* **phi** N = (_P1_-1) * (_P2_-1)

Cocks coined this as the trapdoor for solving **phi**. If you know the factorization for solving _N_, then finding **phi** _N_ is easy.

Example:
* The prime factors of 77 = 7 * 11
* So **phi** 77 = (7-1) * (11-1) = 6 * 10 = 60

He connected the **phi function** to modular exponentiation by using _Euler's theorem_:
* _m_ <sup> **phi** _n_</sup> = 1 mod _n_
* Pick any two numbers that do not share a common factor, say m = 5, and n = 8
* Substitute, 5<sup> **phi** 8</sup> = 1 mod _8_
    * **phi** 8 = 4 as computed earlier
* Simplify, 5 <sup>4</sup> = 1 mod 8
    * 625 = 1 mod 8

Cocks added two modifactions to Euler's theorem:
* Added a k parameter to the exponent
* Multiplied _m_ to both sides of the equation

Resulting in:
* _m_ * _m_ <sup> k * **phi** n </sup> = 1 * _m_ mod _n_
* simplified: _m_ * _m_ <sup> k * **phi** n </sup> = _m_ mod _n_, since 1 * m = m
* and since we're multiplying _m_ * _m_, we can add a +1 to the exponent and remove _m_ from the base multiplication
* finally; _m_ <sup> k * **phi** n + 1 </sup> = _m_ mod _n_

We can now finally calculate _d_ = (k * **phi** n + 1) / e only if the factorization of _n_ is known.

Turning back to Alice and Bob
* Say Bob has a message he converted into a number, _m_, using a padding scheme
* Then Alice generates her public and private key as follows
    * She generates two random prime numbers of similar size, _p1_ = 53, _p2_ = 59
    * Multiplies them together, 53 * 59 = 3127 = _n_
    * Then calculates **phi** _n_ easily because she knows the factorization of _n_
        * **phi** _n_ = **phi** _p1_ * **phi** _p2_
        * _p1_ and _p2_ are primes so **phi** of each p - 1 = (53-1) * (59-1) = 52 * 58
        * so **phi** _n_ = 3016
* Next she picks some small public exponent, _e_, with the condition that she must pick a number that does not share a factor with **phi** _n_
    * In this case we will use _e_ = 3
* Finally, she finds the value of her private exponent, _d_
    * _d_ = 2 (3016) + 1 / 3 = 2011
* She can hide everything except the value of _n_ and _e_ because they make up her public key
* She sends the public key to Bob to lock his message (say, number 89) with
    * Bob does this by taking his message, _m_ <sup> _e_ </sup> mod _n_
        * = 89 <sup>3</sup> mod 3127 = 1394
    * This results in an encrypted message, _c_ = 1394
    * He sends this number back to Alice
* Alice decrypts this message using her private key _d_ = 2011
    * 1394 <sup> 2011 </sup> = 89 mod 3127 = 89, which is Bobs original message!


Notice that Eve, or anyone else with _n_, _c_and _e_ can only find _d_ if they can calcualte **phi** _N_, which requires they know the prime factorization of _N_. With a large enough _N_, Alice can be sure it will take hundreds of years to solve this if _N_ is large enough.

Cocks discovery was immediately deemed classified, until 1977 it was rederived by Ron Rivest, Adi Shamir and Len Adleman, which is why it is now known as RSA.