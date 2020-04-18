def factorial(n):
"""
In mathematics, the factorial of a positive integer n, denoted by n!,
is the product of all positive integers less than or equal to n: For example,
The value of 0! is 1, according to the convention for an empty product

>>> factorial(5)
120

>>> factorial(12)
479,001,600

>>> factorial(0)
1 # tricky, I know!
"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
