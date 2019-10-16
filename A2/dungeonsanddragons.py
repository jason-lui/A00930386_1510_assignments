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
    """
    total = 0

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return total

    # Roll the die the specified times and add rolls to total
    for i in range(number_of_rolls):
        total += random.randint(1, number_of_sides)

    return total


def choose_inventory(inventory):
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
    item_list = []

    print("Welcome to the Olde Tyme Merchant!\n")
    print("Here is what we have for sale:")

    while True:
        for i in range(sorted(inventory)):
            print(f"{i + 1}.{inventory[i]}")
        choice = int(input("What would you like to buy? (-1 to finish)"))
        if choice == -1:
            break
        elif 1 <= choice <= len(inventory):
            item_list.append(inventory[choice - 1])
        else:
            print("You must enter a number corresponding to an item in the list.\n")

    return item_list


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
    char_info["HP"] = roll_hp(char_info["Class"])

    # Roll 3d6 for each stat
    char_info["Strength"] = roll_die(3, 6)
    char_info["Dexterity"] = roll_die(3, 6)
    char_info["Constitution"] = roll_die(3, 6)
    char_info["Intelligence"] = roll_die(3, 6)
    char_info["Wisdom"] = roll_die(3, 6)
    char_info["Charisma"] = roll_die(3, 6)

    # Character starts with 0 experience
    char_info["XP"] = 0

    # Character starts with empty inventory
    char_info["Inventory"] = []

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

    # Print name, class, race, HP, and EXP
    print(f"Your character's name is {character[0]}.\n")
    print(f"Class: {character['Class']}")
    print(f"Race: {character['Race']}")
    print(f"HP: {character['HP'][1]}/{character['HP'][0]}\n")
    print(f"EXP: {character['XP']}")

    # Print character stats
    print("--Attributes--")
    print(f"Strength: {character['Strength']}")
    print(f"Dexterity: {character['Dexterity']}")
    print(f"Constitution: {character['Constitution']}")
    print(f"Intelligence: {character['Intelligence']}")
    print(f"Wisdom: {character['Wisdom']}")
    print(f"Charisma: {character['Charisma']}\n")

    # If the character has an inventory
    if "Inventory" in character.keys():
        print("\n--Inventory--")
        if character["Inventory"]: # Items in the inventory
            for item in character["Inventory"]:
                print(item)
        else: # No items in the inventory
            print("You have no items...")

    return


def select_class():
    """
    !!!
    :return:
    """
    classes = ["fighter", "wizard", "cleric", "rogue", "ranger", "barbarian", "bard",
               "druid", "monk", "paladin", "sorcerer", "warlock"]
    print("Select a class:")
    for i in range(len(classes)):
        print(f"{i + 1}. {classes[i].title()}")

    choice = input("\nChoose a class: ").lower()

    return choice


def select_race():
    """
    !!!
    :return:
    """
    races = ["elf", "halfling", "tiefling", "dragonborn", "dwarf", "gnome", "half-Elf",
             "halfling", "half-Orc"]
    print("Select a race:")
    for i in range(len(races)):
        print(f"{i + 1}. {races[i].title()}")

    choice = input("\nChoose a race: ").lower()

    return choice


def roll_hp(char_class):
    """
    !!!
    :return:
    """
    if char_class in ["sorcerer", "wizard"]:
        hp = roll_die(1, 6)
    elif char_class in ["bard", "cleric", "druid", "monk", "rogue", "warlock"]:
        hp = roll_die(1, 8)
    elif char_class in ["fighter", "paladin", "ranger"]:
        hp = roll_die(1, 10)
    elif char_class in ["barbarian"]:
        hp = roll_die(1, 12)

    return [hp, hp]


def combat_round(opponent_one, opponent_two):
    """
    !!!
    :param opponent_one:
    :param opponent_two:
    :return:
    """
    order = roll_order(opponent_one, opponent_two)

    attack(order[0], order[1])
    attack(order[1], order[0])

    return


def roll_order(bot_1, bot_2):
    """
    !!!
    :param bot_1:
    :param bot_2:
    :return:
    """
    while True:
        roll_1 = roll_die(1, 20)
        roll_2 = roll_die(1, 20)
        if roll_1 > roll_2:
            order = [bot_1, bot_2]
            print(f"{bot_1} will go first.")
            break
        elif roll_2 < roll_1:
            order = [bot_2, bot_1]
            print(f"{bot_2} will go first.")
            break

    return order


def attack(attacker, target):
    """

    :param attacker:
    :param target:
    :return:
    """
    # Print initial HP of the target
    print(f"{target}'s HP: {target['HP'][1]}/{target['HP'][0]}")

    roll = roll_die(1, 20)
    if roll > target["Dexterity"]:
        dmg = roll_die(1, target["HP"][0])
        target["HP"][1] -= dmg
        print("The attack was a success!")
        print(f"{target} took {dmg} damage.")
        if target["HP"][1] <= 0:
            print(f"{target} has died!")
    else:
        print(f"{attacker}'s attack failed!")

    # Print remaining HP of the target
    print(f"{target}'s HP: {target['HP'][1]}/{target['HP'][0]}")

    return


def main():
    """
    !!!
    :return:
    """

    # Ask user for the length of their username
    name_length_1 = int(input("Enter the name length of Player 1: "))
    name_length_2 = int(input("Enter the name length of Player 2: "))

    # create_character() calls roll_die() and create_name()
    # create_name() calls generate_syllable()
    # generate_syllable() calls generate_consonant() and generate_vowel()
    # Inform the users the stats that were rolled
    char_1, char_2 = create_character(name_length_1), create_character(name_length_2)
    print("Rolling stats for characters")
    
    print(f"Player 1 rolled: {char_1['Strength']}, {char_1['Dexterity']}, {char_1['Constitution']}, "
          f"{char_1['Intelligence']}, {char_1['Wisdom']}, {char_1['Charisma']}\n")
    print(f"Player 2 rolled: {char_2['Strength']}, {char_2['Dexterity']}, {char_2['Constitution']}, "
          f"{char_2['Intelligence']}, {char_2['Wisdom']}, {char_2['Charisma']}\n")

    # A list of possible items in the game
    item_list = ['Rabadon\'s Deathcap',
                 'Seraph\'s Embrace',
                 'Liandry\'s Torment',
                 'Morellonomicon',
                 'Warmog\'s Armor',
                 'Randuin\'s Omen',
                 'Banshee\'s Veil',
                 'Abyssal\' Mask',
                 'Infinity Edge',
                 'The Bloodthirster',
                 'Phantom Dancer',
                 'Rapidfire Cannon',
                 'Boots of Lucidity',
                 'Boots of Swiftness',
                 'Boots of Alacrity',
                 'Mercury Treads']

    # Fill the characters inventories with items
    char_1["Inventory"] += choose_inventory(item_list)
    char_2["Inventory"] += choose_inventory(item_list)

    # Print character stats and inventory
    print_character(char_1)
    print_character(char_2)

    # While both characters are alive
    while char_1["hp"][1] > 0 and char_2["hp"][1] > 0:
        combat_round(char_1, char_2)

    return


if __name__ == '__main__':
    doctest.testmod()
    main()

