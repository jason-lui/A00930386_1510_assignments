def cash_money(cad: float) -> dict:
    """

    :param cad:
    :return:
    """
    if cad <= 0:
        print("Money can't be negative.")
        return

    denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    money_dict = {}

    for d in denominations:
        if cad // d > 0:
            money_dict[d] = int(cad // d)
            cad %= d

    return money_dict


# breakdown = cash_money(66.53)
# print(breakdown)
