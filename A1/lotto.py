import doctest


def number_generator():
    """
    Print 6 unique numbers.

    Numbers range from [1, 49].
    :postconditions: generates 6 unique numbers in [1, 49]
    """
    import random

    # Generate a sample of 6 numbers from [1, 49]
    res = random.sample(list(range(50)), 6)

    # Sort res in ascending order
    res.sort()

    # Print res in ascending order in a single line
    print(res[0], res[1], res[2], res[3], res[4], res[5])
    return


def main():
    """
    Drive the program.
    """
    number_generator()


def main():
    """
    Drive the program.
    """
    doctest.testmod()


if __name__ == '__main__':
    main()


# Component(s) of computational thinking

# Pattern Matching and Data Representation
# I chose to represent the randomly generated numbers in a list because the sort() method
# can organize the list in ascending order.

# Algorithms and Automation
# number_generator() uses the randint() function from the random module to generate random numbers.
# The sort() method is also applied to format the list as required.
