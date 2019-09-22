def number_generator():
    """
    Generates and prints 6 unique numbers.

    Numbers range from [1, 49].
    :postconditions: generates 6 unique numbers in [1, 49]
    :return: None
    """
    import random
    res = []
    nums = list(range(50))

    # Generates a number not in res and adds it to res
    n1 = random.choice(nums)
    res.append(n1)
    nums.remove(n1)
    n2 = random.choice(nums)
    res.append(n2)
    nums.remove(n2)
    n3 = random.choice(nums)
    res.append(n3)
    nums.remove(n3)
    n4 = random.choice(nums)
    res.append(n4)
    nums.remove(n4)
    n5 = random.choice(nums)
    res.append(n5)
    nums.remove(n5)
    n6 = random.choice(nums)
    res.append(n6)
    nums.remove(n6)

    # Sorts res in ascending order
    res.sort()

    # Prints res in ascending order in a single line
    print(res[0], res[1], res[2], res[3], res[4], res[5])
    return

# Calls the main function
if __name__ == '__main__':
    number_generator()