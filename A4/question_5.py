import doctest


def cash_money(cad: float) -> dict:
    """
    Determine the minimum amount of currency units needed to represent a floating point number.

    :param cad: a float
    :precondition: cad must be a positive float
    :postcondition: the minimum amount of currency units will be determined
    :return: the amount of each currency unit used to represent the float as a dictionary

    >>> cash_money(0)
    Traceback (most recent call last):
    ...
    Exception: cad cannot be negative.
    >>> cash_money(66.53)
    {50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}
    >>> cash_money(100)
    {100: 1}
    """
    if cad <= 0:
        raise Exception("cad cannot be negative.")

    denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    money_dict = {}

    for d in denominations:
        if cad // d > 0:
            money_dict[d] = int(cad // d)
            cad %= d

    return money_dict


if __name__ == '__main__':
    doctest.testmod()
