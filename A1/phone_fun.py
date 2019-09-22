def number_translator():
    """
    Decodes a phone number that the user inputs.

    :postcondition: the user inputted phone number will be represented as digits
    :return: a string of the phone number containing only digits
    """
    phone = input("Enter a 10-character phone number to be decoded (XXX-XXX-XXXX): ").strip().lower()
    res = ""

    res += decode(phone[0])
    res += decode(phone[1])
    res += decode(phone[2])
    res += decode(phone[3])
    res += decode(phone[4])
    res += decode(phone[5])
    res += decode(phone[6])
    res += decode(phone[7])
    res += decode(phone[8])
    res += decode(phone[9])
    res += decode(phone[10])
    res += decode(phone[11])

    return res

def decode(char):
    """
    Returns the integer equivalent of an alphabetic number on a standard phone.

    :param char: a string
    :precondition: char must be a string of a single alphanumeric character
    :postcondition: the character will be decoded into its integer equivalent
    :return: the corresponding integer as a string
    """
    # char is stripped of its whitespace and made lowercase
    char = char.strip().lower()

    # Retains hyphens and integers
    if char == "-" or char.isnumeric():
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
    else: # char in "wxyz"
        return "9"

# Calls the main function
if __name__ == '__main__':
    print(number_translator())
