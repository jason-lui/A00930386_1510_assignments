import doctest


def im_not_sleepy() -> str:
    """
    Determine the time that requires the most bars to represent on a digital clock.

    :postcondition: the times that requires the most bars will be returned as a string
    :return: a string of the time that requires the most amount of bars
    """
    hours = str(max_bars(1, 12))
    tens = str(max_bars(0, 5))
    minutes = str(max_bars(0, 9))

    max_time = hours + ":" + tens + minutes
    bar_total = time_to_bars(max_time)

    return f"{max_time} uses the most number of bars ({bar_total}) to represent."


def max_bars(lower_bound: int, upper_bound: int) -> int:
    """
    Determine the number within lower_bound and upper_bound that uses the most amount of bars to represent.

    :param lower_bound: an integer
    :param upper_bound: an integer
    :precondition: lower_bound must be a positive integer
    :precondition: upper_bound must be a positive integer
    :postcondition: the number that uses the most amount of bars to represent will be returned
    :return: the number that uses the most amount of bars within lower_bound and upper_bound

    >>> max_bars(1, 12)
    10
    >>> max_bars(0, 5)
    0
    >>> max_bars(0, 9)
    8
    """
    bar_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 10: 8, 11: 4, 12: 7}
    max_bar_value = 0
    max_bar_num = 0

    for i in range(lower_bound, upper_bound):
        if bar_dict[i] > max_bar_value:
            max_bar_value = bar_dict[i]
            max_bar_num = i
    return max_bar_num


def time_to_bars(time_str: str) -> int:
    """
    Convert a time into the number of bars it uses to represent itself.

    :param time_str: a string
    :precondition: time_str must be a string that represents a time
    :postcondition: the number of bars used to represent the time will be returned
    :return: an integer representing the number of bars used to represent the time

    >>> time_to_bars("10:08")
    21
    """
    bar_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 10: 8, 11: 4, 12: 7}
    total_bars = 0

    for char in time_str:
        if char.isnumeric():
            total_bars += bar_dict[int(char)]

    return total_bars


if __name__ == '__main__':
    doctest.testmod()
