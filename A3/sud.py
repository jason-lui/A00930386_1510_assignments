import random
import doctest
import character
import monster


def game():
    """
    Run the maze game until an exit has been found.
    """
    # Initial game state
    char = character.create_character()
    game_board = update_board(char)
    found_exit = False

    # Infinite loop for character movement
    while not found_exit:
        # Tell the user where they are
        print_board(game_board)

        # Get user input and validate input
        direction = get_user_choice()
        valid_move = validate_move(game_board, char, direction)
        if valid_move:
            # Move character and validate exit conditions
            character.move_character(char, direction)
            game_board = update_board(char)
            encounter = monster.create_monster()
            combat_round(char, encounter)
        else:
            print("You can't go in that direction!")


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
    while opponent_one["HP"][1] > 0 and opponent_two["HP"][1] > 0:  # While both players are alive
        order = roll_order(opponent_one, opponent_two)  # Roll for attacking order

        # Characters attack each other
        attack(order[0], order[1])
        attack(order[1], order[0])


def attack(attacker, target):
    """
    Simulates the attacker hitting a target in Dungeons and Dragons.

    :param attacker: a character
    :param target: a character
    :precondition: attacker must be a properly formatted character
    :precondition: target must be a properly formatted character
    :postcondition: the attacker will try to attack the target
    """
    if attacker["HP"][1] <= 0:  # Check if the attacker is dead
        print(f"{attacker['Name']} is dead!")
        return

    print(f"{target['Name']}'s HP: {target['HP'][1]}/{target['HP'][0]}")  # Print initial HP of the target

    roll = roll_die(1, 4)
    if roll == 4:
        print(f"{attacker['Name']}'s attack failed!")
    else:
        dmg = roll_die(1, attacker["Power"])  # Calculate damage
        target["HP"][1] -= dmg
        print(f"The attack was a success!\n{target['Name']} took {dmg} damage.")
        if target["HP"][1] <= 0:
            print(f"{target['Name']} has died!")

    # Print remaining HP of the target
    if target["HP"][1] > 0:
        print(f"{target['Name']}'s HP: {target['HP'][1]}/{target['HP'][0]}\n")


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
            return order
        elif roll_2 > roll_1:
            order = [bot_2, bot_1]
            print(f"\n{bot_2['Name']} will go first.")
            return order
        elif roll_1 == roll_2:
            print(f"Both players rolled {roll_1}! Rolling again...")


def make_board() -> list:
    """
    Generate a 5x5 board.

    0 represents a vacant space, 1 represents an occupied space, 2 represents the exit
    :postcondition: a 5x5 board will be generated with the exit at (4, 4)
    :return: a list of lists of ints representing a 5x5 board
    """
    board = [[0] * 5 for i in range(5)]
    return board


def print_board(board: list):
    """
    Print the board.

    :param board: a list of lists
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be printed as a 2D array

    >>> print_board([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]])
    1 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 2
    >>> print_board([[1,0,0], [0,0,0], [0,0,2]])
    1 0 0
    0 0 0
    0 0 2
    """
    for row in board:
        row_str = ""
        for cell in row:
            row_str += str(cell) + ' '
        print(row_str.strip())


def update_board(character: dict) -> list:
    """
    Update the board with the character's coordinates.

    :param character: a dictionary
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be updated with the character's current position
    :return: the updated board as a list of lists

    >>> update_board({'coords': (0, 0)})
    [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    >>> update_board({'coords': (1, 1)})
    [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    """
    board = make_board()
    x, y = character['coords'][0], character['coords'][1]
    board[y][x] = 1

    return board


def get_user_choice() -> tuple:
    """
    Show the user the available moves and get the user's movement direction

    :postcondition: the user's choice as a tuple containing coords of an xy-plane
    :return: the user's choice as a tuple
    """
    move_coords = {'1': (0, -1), '2': (1, 0), '3': (0, 1), '4': (-1, 0)}

    print("Where would you like to move?")
    print("1. North, 2. East, 3. South, 4. West")
    choice = input("Enter your move (1-4): ")
    while choice not in move_coords.keys():
        print("That is not a valid move.")
        choice = input("Choose a number between 1 and 4: ")
    print('')
    return move_coords[choice]


def validate_move(board: list, character: dict, move: tuple) -> bool:
    """
    Determine if a move is valid.

    :param board: a list of lists
    :param character: a dictionary
    :param move: a tuple
    :precondition: board must be a list of lists of int representing the board
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: direction must be a tuple representing a direction of movement
    :postcondition: the move will be validated
    :return: True or False depending on whether the move is valid

    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, -1))
    False
    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, 1))
    True
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    return True if ((0 <= x <= len(board) - 1) and (0 <= y <= len(board[1]) - 1)) else False


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
    doctest.testmod()
