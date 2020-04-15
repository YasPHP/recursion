from typing import List


def sum(numbers: List[int]):
    """
    Return the total sum of all the elements in the <numbers> lst.

    >>> sum([1, 2, 3, 4])
    10

    >>> sum([2, 2, 2, 2])
    8

    >>> sum([0, 0, 0])
    0
    """

    # base case: if there is no more numbers in the <numbers> lst
    if numbers == []:   # could also be written as "if not numbers", aka if False b/c empty lst, 0 == False
        return 0
    else:
        return numbers[0] + sum(numbers[1:])
        # by the end of it, all of the values of the numbers will be added together
        # ie. sum([1, 2, 3, 4]
        # 1 + sum([2, 3, 4])
        # 1 + 2 + sum([3, 4])
        # 1 + 2 + 3 + sum([4])
        # 1 + 2 + 3 + 4 + sum([])
        # 1 + 2 + 3 + 4 + 0
        # 10
        # ta da! beauty, right?
