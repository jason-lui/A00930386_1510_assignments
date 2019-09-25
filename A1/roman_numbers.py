import doctest


def convert_to_roman_numeral(positive_int):
    """
    Convert a number to its Roman numerals.

    Uses a subset of MDCLXVI. Represents 4 as IV, 9 as IX, etc.

    :param positive_int: a positive integer
    :precondition: positive_int must be positive and in [1, 10000]
    :postcondition: converts positive_int into its Roman numeral
    :return: the Roman numeral as a string

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(28)
    'XXVIII'
    >>> convert_to_roman_numeral(338)
    'CCCXXXVIII'
    >>> convert_to_roman_numeral(4499)
    'MMMMCDXCIX'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    """
    # res stores the result
    res = ""

    # Start concatenating the result starting from the largest denomination
    # Denominations of 1000s
    # Abstract function not used because no denominations higher than 1000
    res += "M" * (positive_int // 1000)

    # Denominations of 100s
    res += roman_denomination(positive_int, 100, "C", "D", "M")

    # Denominations of 10s
    res += roman_denomination(positive_int, 10, "X", "L", "C")

    # Single digits
    res += roman_denomination(positive_int, 1, "I", "V", "X")

    return res


def roman_denomination(num, divisor, ones, fives, tens):
    """
    Generate Roman numeral representation for different orders of magnitude.

    :param num: an integer
    :param divisor: an integer
    :param ones: a string
    :param fives: a string
    :param tens: a string
    :precondition: num must be an integer
    :precondition: divisor must be an integer 10 ** n
    :precondition: ones must be a string representing divisor in Roman numerals
    :precondition: fives must be a string representing divisor * 5 in Roman numerals
    :precondition: tens must be a string representing divisor * 10 in Roman numerals
    :postcondition: produces the Roman numeral representation of a specified order of magnitude
    :return: the Roman numerals for an order of magnitude
    """
    # Strip the number to the desired order of magnitude
    num %= (divisor * 10)

    # Treats the case one ones differentl
    result = ""
    if num // divisor == 4:
        result += ones + fives
        num %= divisor
    elif num // divisor == 9:
        result += ones + tens
        num %= divisor
    else:
        result += fives * (num // (divisor * 5))
        num %= (divisor * 5)
        result += ones * (num// divisor)
        num %= divisor
    return result


# Imports the doctest module to use the tests in the docstring
if __name__ == "__main__":
    doctest.testmod()
