import random


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
    """
    total = 0

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return total

    # Roll the die the specified times and add rolls to total
    for i in range(number_of_rolls):
        total += random.randint(1, number_of_sides)

    return total


def choose_inventory(inventory, selection):
    """
    Choose random items from an inventory.

    Return an empty list if preconditions are not met.
    :param inventory: an integer
    :param selection: an integer
    :precondition: inventory must be a positive integer
    :precondition: selection must be a positive integer
    :postcondition: a list of random items from the inventory will be generated
    :return: a sorted list of random items
    """
    if not inventory and selection == 0:
        return []
    if selection < 0:
        print("WARNING: The number of items selected is negative.")
        return []
    if selection > len(inventory):
        print("WARNING: The number of items selected is larger than the size of the inventory.")
        return sorted(inventory)
    if selection == len(inventory):
        return sorted(inventory)

    # Generates a sorted selection of elements from inventory at random
    random_list = random.sample(inventory, selection)
    return sorted(random_list)


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

    :postcondition: a single random vowel will be generated
    :return: the vowel as a string
    """
    vowel_unicode = [97, 101, 105, 111, 117, 121]
    return chr(random.choice(vowel_unicode))


def generate_consonant():
    """
    Generate a random consonant.

    :postcondition: a single random consonant will be generated
    :return: the random consonant as a string
    """
    consonant_unicode = [98, 99, 100, 102, 103, 104, 106, 107, 108, 109,
                         110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]
    return chr(random.choice(consonant_unicode))


def generate_syllable():
    """
    Generate a syllable containing a random consonant preceding a random vowel.

    :postcondition: a random consonant and a random vowel will be returned
    :return: a string containing a consonant and a vowel
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
    char_info = []
    name = generate_name(name_length)
    char_info.append(name)

    str_stat = roll_die(3, 6)
    strength = ['Strength', str_stat]
    char_info.append(strength)

    dex_stat = roll_die(3, 6)
    dexterity = ['Dexterity', dex_stat]
    char_info.append(dexterity)

    con_stat = roll_die(3, 6)
    constitution = ['Constitution', con_stat]
    char_info.append(constitution)

    int_stat = roll_die(3, 6)
    intelligence = ['Intelligence', int_stat]
    char_info.append(intelligence)

    wis_stat = roll_die(3, 6)
    wisdom = ['Wisdom', wis_stat]
    char_info.append(wisdom)

    cha_stat = roll_die(3, 6)
    charisma = ['Charisma', cha_stat]
    char_info.append(charisma)

    return char_info


def print_character(character):
    """
    Print the information stored within a character info list.

    Index 0 is the character name. Indices 1 to 6 are the stat mini-lists.
    Also accepts an inventory at the 7th index.
    :param character: a list containing the character name, stat mini-lists (and inventory)
    :precondition: character must be a properly formatted list
    :postcondition: character name, stats and inventory will be printed
    """
    print(f"Your character's name is {character[0]}.\n")
    print("--Attributes--")
    for stat in character[1:7]:
        print(f"{stat[0]}: {stat[1]}")

    # If the character has an inventory
    if len(character) == 8:
        print("\n--Inventory--")
        if character[-1]: # Items in the inventory
            for item in character[-1]:
                print(item)
        else: # No items in the inventory
            print("You have no items...")
    return
