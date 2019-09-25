def rock_paper_scissors():
    """
    Play a game of rock paper scissors.

    User inputs rock paper scissors and battles against a randomly generated move.
    :postcondition: generates a win/tie/loss against the user's choice
    """
    # User inputs a string which is stripped and converted to lowercase
    choice = input("Enter rock paper or scissors: ").strip().lower()
    # is_valid() determines if choice is a valid move
    if not is_valid(choice):
        print("You did not input a valid choice. Enter rock paper or scissors.")
        return

    # generate_move() generates a move to match the user input
    move = generate_move()

    if move == choice:
        print(f"The computer chose {move}. It's a tie!")
        return
    if move == "rock":
        if choice == "paper":
            print(f"The computer chose {move}. You win!")
        else: # choice == "scissors"
            print(f"The computer chose {move}. You lose!")
    elif move == "paper":
        if choice == "scissors":
            print(f"The computer chose {move}. You win!")
        else: # choice == "rock"
            print(f"The computer chose {move}. You lose!")
    else: # move == "scissors"
        if choice == "rock":
            print(f"The computer chose {move}. You win!")
        else: # choice == "paper"
            print(f"The computer chose {move}. You lose!")
    return


def is_valid(rps):
    """
    Determine if a string is rock paper or scissors.

    :param choice: a string
    :precondition: choice must be a string
    :return: Boolean
    """
    rps = rps.strip().lower()
    return rps == "rock" or rps == "paper" or rps == "scissors"


def generate_move():
    """
    Generate a move for rock paper scissors.

    :postconditions: generates "rock", "paper" or "scissors"
    :return: a string of "rock", "paper", or "scissors"
    """
    import random
    res = random.randint(0, 2)
    if res == 0:
        return "rock"
    elif res == 1:
        return "paper"
    else: # res == 2
        return "scissors"

# Calls the main function
if __name__ == '__main__':
    rock_paper_scissors()
