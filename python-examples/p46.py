""" @author: Adam, @date 7/1/2019 """

import time

#%% Brute force with no hard-coded upper bounds.

from p3 import is_prime
    
def append_squares(squares, n):
    """Append sorted list of squares up to n."""
    sqrt_max = int(n**.5)
    square = squares[-1]
    sqrt = int(square**.5)
    while sqrt_max > sqrt:
        sqrt += 1
        square = sqrt**2
        squares.append(square)
    return squares

# Keep a growing list of primes and squares and check odd composites.
start = time.time()

primes = [2] 
squares = [1]
n = 3
while True:
    if is_prime(n):
        primes.append(n)
    else:  # n is an odd composite, check Goldbach's other conjecture.
        squares = append_squares(squares, n)
        squares_set = set(squares)
        for prime in primes:
            if (n - prime) % 2 == 0 and (n - prime) // 2 in squares_set:
                break  # out of for loop.
        else:
            print(n)
            break  # out of while loop.
    n += 2

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""