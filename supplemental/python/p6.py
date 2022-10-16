""" @author: Adam, @date: 6-12-2019 """

import numpy as np
import time

def sum_int_sequence(a, b):
    """Sum sequence of integers a, a + 1, ..., b, assuming b > a."""
    term = a + b
    n_terms = (b - a + 1) / 2
    return int(n_terms * term)

#%%
    
start = time.time()
 
# Compute (square of sum) - (sum of squares) for sequence a, a + 1, ..., b.
a = 1
b = 100
sum_of_squares = np.sum(np.arange(a, b+1, 1)**2, dtype = int)
square_of_sum = sum_int_sequence(a, b)**2
print(square_of_sum - sum_of_squares)
            
print(time.time() - start)
