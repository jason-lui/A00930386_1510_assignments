def gcd(a: int, b: int) -> int:
    """
    Determine the greatest common denominator (GCD) of 2 integers.

    :param a: an integer
    :param b: an integer
    :precondition: a must be a non-zero integer
    :precondition: a must be a non-zero integer
    :postcondition: the GCD will be calculated
    :return: the GCD as an integer
    """
    # If either a or b are 0, but not both return the non-zero
    if not a or not b:
        return a if a else b

    while a % b != 0:
        # Set a as the result of a % b
        a %= b

        # Swap the values of a and b for consistency
        a, b = b, a

    return b
