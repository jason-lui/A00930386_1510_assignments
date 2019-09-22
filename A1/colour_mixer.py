def colour_mixer():
    """

    :return:
    """
    # User inputs 2 strings which are converted to lower case
    c1 = input("Enter a primary colour (red, yellow, or blue): ").strip().lower()
    c2 = input("Enter a different primary colour (red, yellow, or blue): ").strip().lower()

    # Prints a helpful message if either colour is not a primary colour
    if c1 != "red":
        if c1 != "yellow":
            if c1 != "blue":
                print("You must enter primary colours (red, yellow, blue).")
                return
    if c2 != "red":
        if c2 != "yellow":
            if c2 != "blue":
                print("You must enter primary colours (red, yellow, blue).")
                return

    # Prints a helpful message if c1 and c2 are the same
    if c1 == c2:
        print("You must enter 2 unique primary colours.")
        return

    # Prints the appropriate secondary colour combination
    if (c1 == "red" and c2 == "blue") or (c1 == "blue" and c2 == "red"):
        print("Purple")
    elif (c1 == "red" and c2 == "yellow") or (c1 == "yellow" and c2 == "red"):
        print("Orange")
    else: # (c1 == "yellow" and c2 == "blue") or (c1 == "blue" and c2 == "yellow")
        print("Green")
    return
