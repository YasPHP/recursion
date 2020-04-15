def recur(word: str) -> int:
    """
    Return the number of characters in the <word> recursively.
    -> Basically an implementation of len() ;P

    >>> recur('beauty')
    6

    >>> recur('yolo')
    4
    """

    # base case: when we reach the end of the word
    if word == '':  # if the word is empty
        return 0    # there are 0 letters
    else:
        return recur(word[1:]) + 1
        # basically shortens the word with every iteration and adds a count for it.

        # looks something like this:
        # recur('olo') + 1
        # recur('lo') +1 +1
        # recur('o') +1 +1 +1
        # recur('') +1 +1 +1 +1
        # 0 +1 +1 +1 +1
        # 4
        # The key idea here is that the recur(something) breaks down into something else that
        # still accurately represents it, albeit more simply!
        # it's like taking a big cake and slicing it into 6 pieces, combined together,
        # all of those 6 pieces still make up the same cake but they represent
        # the cake in a simpler POV of individual littler cakes.
