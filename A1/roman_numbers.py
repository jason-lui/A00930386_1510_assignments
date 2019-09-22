def convert_to_roman_numeral(positive_int):
    """
    Converts a number to its Roman numerals.

    Uses a subset of MDCLXVI. Represents 4 as IIII, 9 as VIIII, etc.

    :param positive_int: a positive integer
    :precondition: positive_int must be positive and in [1, 10000]
    :postcondition: Converts positive_int into its Roman numeral
    :return: The Roman numeral as a string

    >>> convert_to_roman_numeral(0)

    >>> convert_to_roman_numeral(9)
    'VIIII'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    """
    # Checks if positive_int is within [1, 10000]
    if not 1 <= positive_int <= 10000:
        return None
    # res stores the result
    res = ""

    # Start building the result starting from the largest denomination
    res += "M" * (positive_int // 1000)
    positive_int %= 1000
    res += "D" * (positive_int // 500)
    positive_int %= 500
    res += "C" * (positive_int // 100)
    positive_int %= 100
    res += "L" * (positive_int // 50)
    positive_int %= 50
    res += "X" * (positive_int // 10)
    positive_int %= 10
    res += "V" * (positive_int // 5)
    positive_int %= 5
    res += "I" * positive_int

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
