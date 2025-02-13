import doctest


def eratosthenes(n: int) -> list:
    """
    Determine all the prime numbers up to n.

    :param n: an integer
    :precondition: n must be a positive integer
    :postcondition: all primes will be returned
    :return: a list of all the primes up to n

    >>> eratosthenes(-1)
    Traceback (most recent call last):
      ...
    ValueError: n should be a positive integer. The value of n was: -1.
    >>> eratosthenes(1)
    []
    >>> eratosthenes(2)
    [2]
    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    # Raise exception if n is not a positive integer
    if n <= 0:
        raise ValueError(f"n should be a positive integer. The value of n was: {n}.")

    # 0 and 1 are not primes. 2 is prime.
    # Total number of entries is n + 1, so n + 1 - 2 = n - 1
    primes = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:  # Number is prime
            # Sieve the multiples of i
            for multiple in range(i * 2, n + 1, i):
                primes[multiple] = False

    return [i for i, prime in enumerate(primes) if prime]


if __name__ == '__main__':
    doctest.testmod()
