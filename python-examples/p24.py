""" @author: Adam, @date 6/19/2019 

This problem can be solved by hand using the fact that the m-th permutation
can be expressed as a linear combination of factorials whose coefficient
depends on m. Take m = 1,000,000 and permutations of (0, 1, ..., 9). 
There are 10 * 9! permutations. 2 * 9! begin with either 0 or 1, and those
beginning with 3 have order 3 * 9! or higher. Thus we know the first digit is 
2. This process repeats iteratively.
"""

import time

def factorial(n):
    """Return n!."""
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def permutation(order, n):
    """Return the order-th permutation of (0, 1, ..., n - 1)."""
    # List of possible digits.
    digits = []
    for i in range(n):
        digits.append(i)
        
    # Find string representation of permutation, digit by digit.
    order -= 1  # Offset since indexing from 0.
    perm = ''
    for i in range(n):
        digit_order = order // factorial(n - (i+1))
        order -= digit_order * factorial(n - (i+1))
        digit = digits.pop(digit_order)
        perm += str(digit)
        
    return perm
    
#%% Mostly brute force.

start = time.time()

print(permutation(1000000, 10))

print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
1)  Given a permutation, what is its order? See order() function below.
"""

def order(perm, n):
    """Return the order of the permutation of (0, 1, ..., n - 1)."""
    # List of possible digits.
    digits = []
    for i in range(n):
        digits.append(i)
    
    # Find order of permutation.
    order = 1  # Offset since indexing from 0.
    for i in range(n):
        digit = int(perm[i])
        digit_order = digits.index(digit)
        order += digit_order * factorial(n - (i+1))
        del digits[digit_order]
        
    return order

        
        
        
        
        
        
        
        