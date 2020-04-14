def fibonacci(n: int):
    """
    Return the <n> number in a fibonacci sequence.

    The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

    >>> fibonacci(9)
    21

    >>> fibonacci(1)
    0
    """
    # First two are base cases
    if n == 1:  # the defaults I: first <n> element is 0
        return 0
    elif n == 2:  # the defaults II: second <n> element is 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive step
