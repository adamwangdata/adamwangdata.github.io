""" @author: Adam, @date: 6-12-2019 

Brute forcing like I did in 7.py is much slower. Since we have a known limit,
I implement a Sieve of Eratosthenes.
"""

import time
import numpy as np

def get_primes(n):
    """Return numpy array of primes less than n."""
    # Mark all as potentially prime (True) initially except for 0 and 1.
    index_is_prime = np.ones(n, dtype=bool)  
    index_is_prime[0:2] = False
    
    for i in range(2, int(n**.5) + 1):  # Sieve of Eratosthenes.
        if index_is_prime[i]:
            index_is_prime[range(2*i, n, i)] = False
    return(np.where(index_is_prime == True)[0])

#%% Sieve of Eratosthenes. Scales as O(n). 
    
if __name__ == '__main__':    
    start = time.time()
     
    n = 2000000
    primes = get_primes(n)
    print(primes.sum())
    
    print(time.time() - start)


#%%
""" Potential improvements: 
    
"""
