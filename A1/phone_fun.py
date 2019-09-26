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
    if char in "abc":
        return "2"
    elif char in "def":
        return "3"
    elif char in "ghi":
        return "4"
    elif char in "jkl":
        return "5"
    elif char in "mno":
        return "6"
    elif char in "pqrs":
        return "7"
    elif char in "tuv":
        return "8"
    elif char in "wxyz":
        return "9"

    # Return char back if not alphanumeric or "-"
    return char


def main():
    """
    Drive the program.
    """
    print(number_translator())


# Call the main function
if __name__ == '__main__':
    doctest.testmod()

# Component(s) of computational thinking

# Decomposition
# The characters of the phone number is passed to the decode() helper function.
# The corresponding alphabetic number is returned for number_translator().
