def convert_to_roman_numeral(positive_int):
    """
    Converts a number to its Roman numerals.

    Uses a subset of MDCLXVI. Represents 4 as IIII, 9 as VIIII, etc.

    :param positive_int: a positive integer
    :precondition: positive_int must be positive and in [1, 10000]
    :postcondition: converts positive_int into its Roman numeral
    :return: the Roman numeral as a string

    >>> convert_to_roman_numeral(4)
    'IV'
    >>> convert_to_roman_numeral(9)
    'IX'
    >>> convert_to_roman_numeral(39)
    'XXXIX'
    >>> convert_to_roman_numeral(49)
    'XLIX'
    >>> convert_to_roman_numeral(89)
    'LXXXIX'
    >>> convert_to_roman_numeral(99)
    'XCIX'
    >>> convert_to_roman_numeral(399)
    'CCCXCIX'
    >>> convert_to_roman_numeral(499)
    'CDXCIX'
    >>> convert_to_roman_numeral(899)
    'DCCCXCIX'
    >>> convert_to_roman_numeral(999)
    'CMXCIX'
    >>> convert_to_roman_numeral(9999)
    'MMMMMMMMMCMXCIX'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    """
    # Checks if positive_int is within [1, 10000]
    if not 1 <= positive_int <= 10000:
        return None
    # res stores the result
    res = ""

    # Start concatenating the result starting from the largest denomination
    # Denominations of 1000s
    res += "M" * (positive_int // 1000)
    positive_int %= 1000

    # Denominations of 100s
    if positive_int // 100 == 4:
        res += "CD"
        positive_int %= 400
    elif positive_int // 100 == 9:
        res += "CM"
        positive_int %= 900
    else:
        res += "D" * (positive_int // 500)
        positive_int %= 500
        res += "C" * (positive_int // 100)
        positive_int %= 100

    # Denominations of 10s
    if positive_int // 10 == 4:
        res += "XL"
        positive_int %= 40
    elif positive_int // 10 == 9:
        res += "XC"
        positive_int %= 90
    else:
        res += "L" * (positive_int // 50)
        positive_int %= 50
        res += "X" * (positive_int // 10)
        positive_int %= 10

    # Single digits
    if positive_int == 4:
        res += "IV"
    elif positive_int == 9:
        res += "IX"
    else:
        res += "I" * positive_int

    return res


# Imports the doctest module to use the tests in the docstring
if __name__ == "__main__":
    import doctest
    doctest.testmod()
