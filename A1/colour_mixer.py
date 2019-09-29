import doctest


def colour_mixer():
    """
    Combine 2 primary colours into a secondary colour.

    User inputs 2 unique primary colours.
    :postcondition: prints the resulting secondary colour if inputs are valid
    """
    # User inputs 2 strings which are stripped of whitespace and converted to lowercase
    c1 = input("Enter a primary colour (red, yellow, or blue): ").strip().lower()
    c2 = input("Enter a different primary colour (red, yellow, or blue): ").strip().lower()

    # is_primary() determines if c1 and c2 are primary colours
    # Print a helpful message if either colour is not a primary colour
    if not is_primary(c1) or not is_primary(c2):
        print("Both colours must be primary colours (red, yellow, blue).")
        return

    # Print a helpful message if c1 and c2 are the same
    if c1 == c2:
        print("You must enter 2 unique colours.")
        return

    # Print the appropriate secondary colour combination
    if (c1 == "red" and c2 == "blue") or (c1 == "blue" and c2 == "red"):
        print("Purple")
    elif (c1 == "red" and c2 == "yellow") or (c1 == "yellow" and c2 == "red"):
        print("Orange")
    else: # (c1 == "yellow" and c2 == "blue") or (c1 == "blue" and c2 == "yellow")
        print("Green")


def is_primary(colour):
    """
    Determine if a colour is a primary colour.

    :param colour: a string
    :precondition: colour must be a string of "red", "yellow" or "blue" (case insensitive)
    :postcondition: determines if colour is a primary colour
    :return: Boolean

    >>> is_primary('red')
    True
    >>> is_primary('yellow')
    True
    >>> is_primary('blue')
    True
    >>> is_primary('purple')
    False
    """
    # Strip whitespace and converts string to lower case
    colour = colour.strip().lower()
    return colour == "red" or colour == "yellow" or colour == "blue"


def main():
    """
    Drive the program.
    """
    colour_mixer()
    doctest.testmod()


if __name__ == '__main__':
    main()


# Component(s) of computational thinking

# Decomposition
# colour_mixer() uses decomposition by incorporating a is_primary() as a helper function.
# is_primary() checks if the user input is a primary colour. This helper function can be
# used in any program that requires a function to verify primary colours.
