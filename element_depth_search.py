def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """ Return the first (leftmost) number in <obj> at depth <d>.

     Return None if there is no item at depth d.

     Precondition: d >= 0.

     >>> first_at_depth(100, 0)
     100
     >>> first_at_depth(100, 3) is None
     True
     >>> first_at_depth([10, [[20]], [30, 40]], 2)
     30
     >>> first_at_depth([10, [[20]], [30, 40]], 0) is None
     True
     """
    # if isinstance(obj, int):
    #     return obj
    #
    # if d == 0:
    #     return 0
    #
    # else:
    #     return first_at_depth(obj[1:], d - 1)

    if d == 0:
        if isinstance(obj, int):
            return obj
        else:
            return None

    else:   # obj assumed to be a list
        status = None
        if isinstance(obj, list):
            for sublist in obj:
                if status is not None:
                    status = status
                else:
                    first_at_depth(sublist, d - 1)
        return status
