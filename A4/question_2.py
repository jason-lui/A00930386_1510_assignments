import doctest


def gcd(a: int, b: int) -> int:
    """
    Determine the greatest common divisor (GCD) of 2 integers.

    :param a: an integer
    :param b: an integer
    :precondition: a must be a non-zero integer
    :precondition: b must be a non-zero integer
    :postcondition: the GCD will be calculated
    :return: the GCD as an integer

    >>> gcd(0, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Neither a or b can be 0.
    >>> gcd(5, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Neither a or b can be 0.
    >>> gcd(-25, 15)
    5
    >>> gcd(30, 12)
    6
    >>> gcd(36, 123)
    3
    >>> gcd(7, 7)
    7
    """
    # Raise exception if either a or b are 0
    if not a or not b:
        raise ZeroDivisionError("Neither a or b can be 0.")

    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a %= b  # Set a as the result of a % b
        a, b = b, a  # Swap the values of a and b for consistency
    return abs(b)


if __name__ == '__main__':
    doctest.testmod()
