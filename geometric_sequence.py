from typing import List


def geometric_sequence(a: int, r: int, length: int) -> List[int]:
    """
    Return a subsequent geometric sequence with a <length>
    generated from the <start> as a starting point combined
    with a <multiplier>.

    In General we write a Geometric Sequence like this:

    {a, ar, ar2, ar3, ... }

    where:
    a is the first term, and
    r is the factor between the terms (called the "common ratio") -> the multiplier

    >>> geometric_sequence(1, 2, 5)
    [1, 2, 4, 8, 16]

    >>> geometric_sequence(10, 10, 3)
    [10, 100, 1000]

    >>> geometric_sequence(3, 9, 2)
    [3, 27]
    """
    # base case: if the length of the list gets reached

    if length == 0:
        return []

    else:
        return [a] + geometric_sequence(a * r, r, length - 1)

        # always note that in recursion, the PARAMETERS CHANGE
        # through each stack frame added to the call stack!
        # take advantage of that dynamism.

        # Ie. here we BUILT A LIST through the dynamistic nature of recursion.
        # The lists build up over time and all concatenate once the call stack
        # progressively gets top-down dominated ;O
        # geometric_sequence(1, 2, 5)
        # [1] + geometric_sequence(2, 2, 4)
        # [1] + [2] + geometric_sequence(4, 2, 3)
        # [1] + [2] + [4] + geometric_sequence(8, 2, 2)
        # [1] + [2] + [4] + [8] + geometric_sequence(16, 2, 1)
        # [1] + [2] + [4] + [8] + [16] + geometric_sequence(32, 2, 0)
        # [1] + [2] + [4] + [8] + [16] + [32] + []
        # [1, 2, 4, 8, 16, 32]
        # voila et à bientôt!


