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
    # List of the desired time frames and their values in seconds
    seconds_per_day = 86400
    seconds_per_hour = 3600
    seconds_per_minute = 60

    # Separate desired time frames into variables
    days = time_converter(seconds, seconds_per_day)
    seconds %= seconds_per_day
    hours = time_converter(seconds, seconds_per_hour)
    seconds %= seconds_per_hour
    minutes = time_converter(seconds, seconds_per_minute)
    seconds %= seconds_per_minute

    print(days, hours, minutes, seconds)
    return


def time_converter(seconds, time_frame):
    """
    Convert seconds to the specified time frame.

    :param seconds: an integer
    :param time_frame: an integer
    :precondition: time_frame must be an integer
    :postcondition: the returned amount of time is an integer
    :return: the seconds divided by the time_frame as an integer

    >>> time_converter(3000, 3600)
    0
    >>> time_converter(4000, 3600)
    1
    """
    return seconds // time_frame


def main():
    """
    Drive the program.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()


# Component(s) of computational thinking

# Decomposition
# time_calculator() uses the helper function time_converter() to calculate the
# number of days/hours/minutes given a number of seconds. The helper function
# can be implemented into any program that requires a conversion of time if given seconds.
