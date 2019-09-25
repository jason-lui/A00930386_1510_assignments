import doctest


def time_calculator(seconds):
    """
    Convert the number of seconds into days, hours, minutes, seconds.

    :param seconds: an integer
    :precondition: seconds must be a positive integer
    :postcondition: the days, hours, minutes, seconds will be printed

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(100000)
    1 3 46 40
    """
    # Check if seconds is an integer
    if seconds != int(seconds):
        return

    # List of the desired time frames and their values in seconds
    days_sec = 86400
    hours_sec = 3600
    minutes_sec = 60

    # Separate desired time frames into variables
    days = seconds // days_sec
    seconds %= days_sec
    hours = seconds // hours_sec
    seconds %= hours_sec
    minutes = seconds // minutes_sec
    seconds %= minutes_sec

    print(days, hours, minutes, seconds)
    return


# Import the doctest module to use the tests in the docstring
if __name__ == "__main__":
    doctest.testmod()
