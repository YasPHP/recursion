def reverse(word: str) -> str:
    """
    Return the inputted <word> in reverse via recursion love.

    >>> reverse("hello")
    'olleh'
    """

    # base case: when we reach the end of the str
    if word == "":  # return the actual word itself or empty str if there is none
        return word
    else:
        return reverse(word[1:]) + word[0]
        # each time it decomposes the problem to sub problems via shortening
        # the str it has to deal with each time and taking the first element
        # out to create a reversed impression
        # ultimately, it will result in something like:
        # reverse('o') + 'l' + 'l' + 'e' + 'h'
        # -> it accumulates lovely when you start collapsing all the stacks
        # because their data relies on each other, till you get something like:
        # 'o' 'l' 'l' 'e' 'h'
