
  
def recur_sum(n): 
    """
    Return sum of natural numbers up to the <n> indicated.
    
    >>> print(recur_sum(5)) 
    15

    
    >>> print(recur_sum(1)) 
    1

    
    >>> print(recur_sum(0)) 
    0

    """

    if n <= 1: # base case: when first element is reached

        return n 

    return n + recur_sum(n - 1) # recursive call: dominoes to previous sums to accumulate.

  


