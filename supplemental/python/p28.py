""" @author: Adam, @date 6/19/2019 

Recycle is_prime() from 3.py.
"""

import time

def is_prime(n):
    """Return True if n is prime and False otherwise."""
    for i in range(2, int(n**(.5)) + 1):  # int() takes the floor for us
        if n % i == 0:
            return False
    return True

#%% Brute force.

start = time.time()

# Loop over range of a, b and compute chain lengths.
max_chain = 0
max_prod = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):   
        chain = 0
        prod = a*b
        n = 0
        while True:
            quad = n**2 + a*n + b
            if quad > 0 and is_prime(quad):
                chain += 1
                n += 1
            else:
                break
        if chain > max_chain:
            max_chain = chain
            max_prod = prod
print("chain: ", max_chain, "prod: ", max_prod)
    

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Use a faster is_prime() function, e.g. a sieve of Eratosthenes.
2)  Restrict loop over b to be primes, since when = 0, quad = b. This can be
    done using a sieve of Eratosthenes.
    
    Extensions / Remarks:
"""
        
        
        
        
        
        