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
    Exception: Both a and b cannot be 0.
    >>> gcd(5, 0)
    5
    >>> gcd(-5, 0)
    -5
    >>> gcd(30, 12)
    6
    >>> gcd(36, 123)
    3
    """
    # Raise exception if both a and b are 0
    if not a and not b:
        raise Exception("Both a and b cannot be 0.")

    # If either a or b are 0, but not both return the non-zero
    if not a or not b:
        return a if a else b

    a, b = max(a, b), min(a, b)

    while a % b != 0:
        a %= b  # Set a as the result of a % b
        a, b = b, a  # Swap the values of a and b for consistency
    return b


if __name__ == '__main__':
    doctest.testmod()
