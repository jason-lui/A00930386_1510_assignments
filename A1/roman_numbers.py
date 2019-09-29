import doctest


def convert_to_roman_numeral(positive_int):
    """
    Convert a number to Roman numerals.

    Uses a subset of M, D, C, L, X, V, I.
    Represents 4 as IV, 9 as IX, etc.
    :param positive_int: a positive integer
    :precondition: positive_int must be positive and in [1, 10000]
    :postcondition: converts positive_int into Roman numerals
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

    # Start concatenating the result starting from the order of magnitude
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
    :precondition: divisor must be an integer that is a power of 10 (1, 10, 100...)
    :precondition: ones must be a string representing divisor in Roman numerals
    :precondition: fives must be a string representing divisor * 5 in Roman numerals
    :precondition: tens must be a string representing divisor * 10 in Roman numerals
    :postcondition: produces the Roman numeral representation of a specified order of magnitude
    :return: the Roman numerals for an order of magnitude

    >>> roman_denomination(4321, 100, "C", "D", "M")
    'CCC'
    >>> roman_denomination(4321, 10, "X", "L", "C")
    'XX'
    >>> roman_denomination(4321, 1, "I", "V", "X")
    'I'
    """
    # Strip the number to the desired order of magnitude
    num %= (divisor * 10)

    # Concatenate string in result
    result = ""

    # Use exceptions for 4 and 9 cases
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


def main():
    """
    Drive the program.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()


# Component(s) of computational thinking

# Abstraction and Generalization
# convert_to_roman_numeral() uses the roman_denomination() abstract function to
# break down a number by order of magnitudes.
# I recognized that the process for converting and 1s, 10s, 100s were the same.
# Each level represents the 4 and 9 cases in a similar way. The 1000s didn't use
# the abstract function because we don't use denominations higher than that.
# If the subset of numbers and the range of inputs were larger, the abstract function
# can accept larger denominations for larger numbers.
