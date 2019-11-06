import doctest


def create_character():
    """
    Generate a character with 10 HP.

    :postcondition: a character with 10 HP will be generated as a dictionary
    :return: a character with 10 HP represented as a dictionary
    """
    char_info = {}

    char_info['Name'] = "Link"
    char_info['coords'] = 10
    char_info['HP'] = 10
    char_info['Power'] = 6
    return char_info


def move_character(character: dict, move: tuple) -> dict:
    """
    Move a character 1 space on the board.

    :param character: a dictionary
    :param move: a string
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: move must be a string representing a cardinal direction
    :return: a dictionary containing the updated coordinates

    >>> move_character({'coords': (0, 0)}, (0, 1))
    {'coords': (0, 1)}
    >>> move_character({'coords': (0, 0)}, (1, 0))
    {'coords': (1, 0)}
    >>> move_character({'coords': (1, 1)}, (0, -1))
    {'coords': (1, 0)}
    >>> move_character({'coords': (1, 1)}, (-1, 0))
    {'coords': (0, 1)}
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    character['coords'] = (x, y)
    return character


if __name__ == '__main__':
    doctest.testmod()
