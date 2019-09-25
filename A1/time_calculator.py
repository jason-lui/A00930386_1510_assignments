import doctest


def time_calculator(seconds):
    """
    Converts the number of seconds into days, hours, minutes, seconds.

    :param seconds: an integer
    :precondition: seconds must be a positive integer
    :postcondition: the days, hours, minutes, seconds will be printed
    :return: None

    >>> time_calculator(-1)

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(100000)
    1 3 46 40
    """
    # Returns None if seconds is less than 0
    if seconds < 0:
        return None

    # Separates days, hours, minutes and seconds
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print(days, hours, minutes, seconds)
    return


# Imports the doctest module to use the tests in the docstring
if __name__ == "__main__":
    doctest.testmod()
