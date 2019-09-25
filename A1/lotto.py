def number_generator():
    """
    Generate and print 6 unique numbers.

    Numbers range from [1, 49].
    :postconditions: generates 6 unique numbers in [1, 49]
    """
    import random

    # Generates a sample of 6 numbers from [1, 49]
    res = random.sample(list(range(50)), 6)

    # Sorts res in ascending order
    res.sort()

    # Prints res in ascending order in a single line
    print(res[0], res[1], res[2], res[3], res[4], res[5])
    return


# Call the main function
if __name__ == '__main__':
    number_generator()