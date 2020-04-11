"""
The Tower of Hanoi problem!
"""


def move(f, t):
    """
    >>> move(1, 2)
    'move disc from 1 to 2'

    >>> move('A', 'B')
    'move disc from A to B'
    """
    return "move disc from {} to {}".format(f, t)


def hanoi(n, f, h, t):
    """
    >>> hanoi(4, "A", "B", "C")
    'move disc from 1 to 2'

    >>> move('A', 'B')
    'move disc from A to B'
    """
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)


hanoi(4, "A", "B", "C")
