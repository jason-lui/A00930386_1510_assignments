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
    ValueError: cad must be a positive float with max 2 decimal places.
    >>> cash_money(6.553)
    Traceback (most recent call last):
    ...
    ValueError: cad must be a positive float with max 2 decimal places.
    >>> cash_money(66.53)
    {50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}
    >>> cash_money(99.99)
    {50: 1, 20: 2, 5: 1, 2: 2, 0.25: 3, 0.1: 2, 0.01: 4}
    >>> cash_money(100)
    {100: 1}
    """
    if cad <= 0 or cad != round(cad, 2):
        raise ValueError("cad must be a positive float with max 2 decimal places.")

    money_dict = {}
    big_d = [100, 50, 20, 10, 5, 2, 1]
    small_d = [25, 10, 5, 1]  # in cents
    dollars = int(cad)
    cents = round((cad - dollars) * 100, 2)

    for d in big_d:
        while dollars >= d:
            money_dict[d] = int(dollars // d)
            dollars %= d
    for d in small_d:
        while cents >= d:
            money_dict[d / 100] = int(cents // d)
            cents %= d

    return money_dict


if __name__ == '__main__':
    doctest.testmod()
