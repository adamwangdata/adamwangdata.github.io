""" @author: Adam, @date: 6-11-2019 """

import numpy as np
import time

def find_multiples(n, m):
    """ Return list of all multiples of m less than or equal to n."""
    n_multiples = n//m
    multiples = np.arange(1, n_multiples + 1) * m
    return multiples

#%% Vectorized solution. 
start = time.time()     

n = 999
mult3 = find_multiples(n, 3)    
mult5 = find_multiples(n, 5)    
mult = np.union1d(mult3, mult5)
print(mult.sum())

print(time.time() - start)