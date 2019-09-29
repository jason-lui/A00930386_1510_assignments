import doctest


def number_translator():
    """
    Decode an alphanumeric phone number into numbers.
    .
    The user inputs a phone number in the form of XXX-XXX-XXXX.
    :postcondition: the user inputted phone number will be represented as digits
    :return: a string of the phone number containing only digits
    """
    phone = input("Enter a 10-character phone number to be decoded (XXX-XXX-XXXX): ").strip().lower()

    # Concatenates result
    return decode(phone[0]) + decode(phone[1]) + decode(phone[2]) + decode(phone[3]) + \
           decode(phone[4]) + decode(phone[5]) + decode(phone[6]) + decode(phone[7]) + \
           decode(phone[8]) + decode(phone[9]) + decode(phone[10]) + decode(phone[11])


def decode(char):
    """
    Return the integer equivalent of a letter on a standard phone.

    :param char: a string
    :precondition: char must be a string of a single alphanumeric character
    :postcondition: the character will be decoded into its integer equivalent
    :return: the corresponding integer as a string

    >>> decode('1')
    '1'
    >>> decode('a')
    '2'
    >>> decode('%')
    '%'
    """
    # char is stripped of its whitespace and made lowercase
    char = char.strip().lower()

    # Retain hyphens and integers
    if char == "-" or char in "1234567890":
        return char

    # char is converted to its associated integer
    if char == "a" or char == "b" or char == "c":
        return "2"
    elif char == "d" or char == "e" or char == "f":
        return "3"
    elif char == "g" or char == "h" or char == "i":
        return "4"
    elif char == "j" or char == "k" or char == "l":
        return "5"
    elif char == "m" or char == "n" or char == "o":
        return "6"
    elif char == "p" or char == "q" or char == "r" or char == "s":
        return "7"
    elif char == "t" or char == "u" or char == "v":
        return "8"
    elif char == "w" or char == "x" or char == "y" or char == "z":
        return "9"

    # Return char back if not alphanumeric or "-"
    return char


def main():
    """
    Drive the program.
    """
    print(number_translator())
    doctest.testmod()


if __name__ == '__main__':
    main()


# Component(s) of computational thinking

# Decomposition
# The characters of the phone number is passed to the decode() helper function.
# The corresponding alphabetic number is returned for number_translator().
