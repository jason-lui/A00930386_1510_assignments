import doctest


def monster():
    """
    Generate a monster with 5 HP.

    :postcondition: a monster with 5 HP will be generated as a dictionary
    :return: a monster with 5 HP represented as a dictionary
    """
    monster_info = {}

    monster_info['HP'] = [5, 5]
    monster_info['Power'] = 6
    monster_info['Backstab'] = 4
    return monster_info
