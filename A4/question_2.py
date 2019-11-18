def gcd(a: int, b: int) -> int:
    """

    :param a:
    :param b:
    :return:
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
