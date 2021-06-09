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


def encode(message, substitution_table):
    # return "".join(substitution_table.get(x, x) for x in message)

    cipher = ""
    for letter in message:
        if letter in substitution_table:
            cipher += substitution_table[letter]
        else:
            cipher += letter

    return cipher


def decode(message, substitution_table):
    return encode(message, substitution_table)


def printable_substitution(substitution_table):
    # Sort by source character so things are alphabetized.
    mapping = sorted(substitution_table.items())

    # Then create two lines: source above, target beneath
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(substitution_letter for _, substitution_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)


if __name__ == "__main__":
    shift = 1
    encoding, decoding = create_shift_substitutions(shift)
    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(shift))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.n\n")

        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))
        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))
        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))
        elif choice == '4':
            new_shift = input("\nNew shift (currently {}): ".format(shift))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                shift = new_shift
                encoding, decoding = create_shift_substitutions(shift)
        elif choice == '5':
            print("Terminating. This program will self destruct in 5 seconds.\n")
            break
        else:
            print("Unknown option {}.".format(choice))
