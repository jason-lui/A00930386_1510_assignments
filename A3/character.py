import doctest


def create_character():
    """
    Generate a character with 10 HP.

    :postcondition: a character with 10 HP will be generated as a dictionary
    :return: a character with 10 HP represented as a dictionary
    """
    char_info = {}

    char_info["HP"] = 10
    char_info["Power"] = 6
    return char_info


if __name__ == '__main__':
    doctest.testmod()
