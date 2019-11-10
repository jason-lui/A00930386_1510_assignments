import random


def create_monster():
    """
    Generate a monster with 5 HP.

    :postcondition: a monster with 5 HP will be generated as a dictionary
    :return: a monster with 5 HP represented as a dictionary
    """
    mob_list = ['Goblin', 'Goomba', 'Minion', 'Bandit', 'Highwayman', 'Troll']
    monster_info = {}

    monster_info['name'] = random.choice(mob_list)
    monster_info['max_hp'] = 10
    monster_info['current_hp'] = 10
    monster_info['power'] = 6
    monster_info['backstab'] = 4
    return monster_info
