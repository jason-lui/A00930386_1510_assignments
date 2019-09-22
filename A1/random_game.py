def rock_paper_scissors():
    """
    Plays a game of rock paper scissors.

    User inputs rock paper scissors and battles against a randomly generated move.
    :return: None
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



