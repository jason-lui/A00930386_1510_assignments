import doctest


def compound_interest(principal, rate, times_compounded, years):
    """
    Calculate the balance after compounding interest over time.

    The rate is given as a decimal (i.e. 1.13 represents 13%). A is rounded to 2 decimal places.
    :param principal: a float
    :param rate: a float
    :param times_compounded: an integer
    :param years: an integer
    :precondition: principal must be a positive float
    :precondition: annual_rate must be a positive float
    :precondition: times_compounded must be a positive integer
    :precondition: principal must be a positive integers
    :postcondition: calculates the balance after compound interests
    :return: the calculated balance as a float

    >>> compound_interest(0, 0, 0, 0)
    0
    >>> compound_interest(100.01, 0, 10, 10)
    100.01
    >>> compound_interest(100.01, 10, 0, 10)
    100.01
    >>> compound_interest(100.01, 10, 10, 0)
    100.01
    >>> compound_interest(10, 1.13, 3, 5)
    60.87
    """
    # Return principal if any input = 0
    if principal == 0 or rate == 0 or times_compounded == 0 or years == 0:
        return principal

    # Calculate A, the balance after the elapsed time
    A = principal * (1 + rate / times_compounded) ** (rate * years)

    # Return A rounded to 2 decimal places
    return round(A, 2)


def main():
    """
    Drive the program.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()


# Component(s) of computational thinking

# Pattern Matching and Data Representation
# I recognized that the input will equal the output if parameter is 0.
# Once I noticed this pattern, I added a boolean statement to return the principal in these cases.
# Noticing the pattern in outputs allowed to create a shortcut for this problem.
