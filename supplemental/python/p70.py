""" @author: Adam, @date 7-29-2019

Totient sieve based on Euler product formula. """

import time 
import numpy as np

#%% Compute phi(n) for all n using a sieve based on Euler's product formula. 

from p10 import get_primes
from p49 import are_permutations

def get_totients(n):
    """Return numpy array of all totients phi(i), i in [1, n]."""
    totient_array = np.arange(1, n+1, 1, dtype = float)
    for i in range(2, n+1):    
        if totient_array[i-1] == i:  # Unmodified, thus prime
            # Apply Euler's product formula. All multiples of a prime will
            # contain that distinct prime factor.
            totient_array[range((i-1), n, i)] *= 1 - 1/i
    return totient_array

def get_totient_permutations(totients):
    """Given an array of sequential totients starting from phi(1) = 1, return
    list of all totients phi(n) = m such that n and are permutations, excluding
    n = m = 1. List contains tuples (n/m, n, m)."""
    totient_list = []
    for i in range(2, len(totients)):
        totient_i = int(phi_array[i-1])
        if are_permutations(i, totient_i):
            totient_list.append((i/totient_i, i, totient_i))
    return totient_list    
        

if __name__ == '__main__':
    start_time = time.time()    
    
    n = int(1e6)
    phi_array = get_totients(n)
    phi_perm_list = get_totient_permutations(phi_array)
    print(min(phi_perm_list))
    
    print(time.time() - start_time)


#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""


    
    
    
    
    