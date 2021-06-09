import string


# create shift substitution table
def create_shift_substitutions(shift):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i % shift) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter

    return encoding, decoding


def encode(message, substitution):
    cipher = ""
    for letter in message:
        if letter in substitution:
            cipher += substitution[letter]
        else:
            cipher += letter

    return cipher


def decode(message, substitution):
    return encode(message, substitution)
