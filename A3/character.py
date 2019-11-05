import random
import doctest


def generate_name(syllables):
    """
    Generate a name containing the specified number of syllables.

    :param syllables: an integer
    :precondition: syllables must be a positive integer
    :postcondition: a name with the correct number of syllables will be generated
    :return: the string with the correct number of syllables in title case
    """
    name = ""

    # Generate name with the specified number of syllables
    for i in range(syllables):
        name += generate_syllable()

    return name.title()


def generate_vowel():
    """
    Generate a random vowel (y included).

    :postcondition: a single random vowel will be generated in lower case
    :return: the vowel as a string
    """
    vowels = ["a", "e", "i", "o", "u", "y"]

    return random.choice(vowels)


def generate_consonant():
    """
    Generate a random consonant.

    :postcondition: a single random consonant will be generated in lower case
    :return: the random consonant as a string
    """
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                  "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    return random.choice(consonants)


def generate_syllable():
    """
    Generate a syllable containing a random consonant preceding a random vowel.

    :postcondition: a random consonant and a random vowel will be returned
    :return: a string containing a consonant and a vowel in lower case
    """
    return generate_consonant() + generate_vowel()


def create_character(name_length):
    """
    Generate a character's name and attributes.

    Attributes are strength, dexterity, constitution, intelligence, wisdom, and charisma.
    Attributes are rolled using 3 6-sided dice.
    :param name_length: an integer
    :precondition: name_length must be a positive integer
    :postcondition: a character's name, and attributes will be generated
    :return: a list containing a character's name and attributes
    """
    # Start dictionary
    char_info = {}

    # Generate name and add to dictionary
    name = generate_name(name_length)
    char_info["Name"] = name

    # User selects a class and race
    char_info["Class"] = select_class()
    char_info["Race"] = select_race()

    # Character's hit points
    char_info["HP"] = 10

    # Character starts with 0 experience
    char_info["XP"] = 0

    # Character starts with empty inventory
    char_info["Inventory"] = []
    return char_info


def select_class():
    """
    Select a class from Dungeons and Dragons.

    User inputs a number corresponding to a class.
    :postcondition: a class will be selected
    :return: the class as a string in lower case
    """
    classes = ["fighter", "wizard", "cleric", "rogue", "ranger", "barbarian", "bard",
               "druid", "monk", "paladin", "sorcerer", "warlock"]

    print("Select a class:")
    for i in range(len(classes)):
        print(f"{i + 1}. {classes[i].title()}")

    choice = int(input(f"\nChoose a class (1-{len(classes)}): "))
    choice = classes[choice - 1]

    return choice


def select_race():
    """
    Select a race from Dungeons and Dragons.

    User inputs a number corresponding to a race.
    :postcondition: a race will be selected
    :return: the race as a string in lower case
    """
    races = ["elf", "halfling", "tiefling", "dragonborn", "dwarf", "gnome", "half-elf",
             "human", "half-orc"]
    print("Select a race:")
    for i in range(len(races)):
        print(f"{i + 1}. {races[i].title()}")

    choice = int(input(f"\nChoose a race (1-{len(races)}): "))
    choice = races[choice - 1]

    return choice








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


if __name__ == '__main__':
    doctest.testmod()
