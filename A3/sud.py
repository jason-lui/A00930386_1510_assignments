import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total.

    Return 0 if either parameter is not a positive integer.
    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls must be a positive integer
    :precondition: number_of_sides must be a positive integer
    :postcondition: the sum from the die rolls will be totaled
    :return: the total of the die rolls as an integer

    >>> roll_die(0, 0)
    0
    >>> roll_die(0, 10)
    0
    >>> roll_die(10, 0)
    0
    """
    total = 0

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return total

    # Roll the die the specified times and add rolls to total
    for i in range(number_of_rolls):
        total += random.randint(1, number_of_sides)

    return total


def combat_round(opponent_one, opponent_two):
    """
    Simulate one round of combat between characters.

    Players will to determine attacking order.
    Each character attacks once.
    :param opponent_one: a character
    :param opponent_two: a character
    :precondition: opponent_one must be a properly formatted character
    :precondition: opponent_two must be a properly formatted character
    :postcondition: a battle will be simulated
    """
    # Roll for attacking order
    order = roll_order(opponent_one, opponent_two)

    # Characters attack each other
    attack(order[0], order[1])
    attack(order[1], order[0])

    return


def attack(attacker, target):
    """
    Simulates the attacker hitting a target in Dungeons and Dragons.

    :param attacker: a character
    :param target: a character
    :precondition: attacker must be a properly formatted character
    :precondition: target must be a properly formatted character
    :postcondition: the attacker will try to attack the target
    """
    # Check if the attacker is dead
    if attacker["HP"][1] <= 0:
        print(f"{attacker['Name']} is dead!")
        return

    # Print initial HP of the target
    print(f"{target['Name']}'s HP: {target['HP'][1]}/{target['HP'][0]}")

    # Calculate damage
    roll = roll_die(1, 20)
    if roll > target["Dexterity"]:
        dmg = roll_die(1, attacker["HP"][0])
        target["HP"][1] -= dmg
        print("The attack was a success!")
        print(f"{target['Name']} took {dmg} damage.")
        if target["HP"][1] <= 0:
            print(f"{target['Name']} has died!")
    else:
        print(f"{attacker['Name']}'s attack failed!")

    # Print remaining HP of the target
    if target["HP"][1] > 0:
        print(f"{target['Name']}'s HP: {target['HP'][1]}/{target['HP'][0]}\n")

    return


def roll_order(bot_1, bot_2):
    """
    Determine the attacking order for a battle round in Dungeons and Dragons.

    Each character rolls 1d20 and the higher roll goes first.
    Rolls until an order is determined.
    :param bot_1: a character
    :param bot_2: a character
    :precondition: bot_1 must be a properly formatted character
    :precondition: bot_2 must be a properly formatted character
    :postcondition: the attacking order will be determined
    :return: the attacking order as a list of characters
    """
    while True:
        roll_1 = roll_die(1, 20)
        roll_2 = roll_die(1, 20)
        if roll_1 > roll_2:
            order = [bot_1, bot_2]
            print(f"\n{bot_1['Name']} will go first.")
            break
        elif roll_2 > roll_1:
            order = [bot_2, bot_1]
            print(f"\n{bot_2['Name']} will go first.")
            break
        elif roll_1 == roll_2:
            print(f"Both players rolled {roll_1}! Rolling again...")

    return order
