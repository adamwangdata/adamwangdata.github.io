""" @author: Adam, @date: 6-25-2019 """

from p3 import is_prime
import time 
import itertools as it
import numpy as np

def get_ndigitals(n):
    """Construct all n-digit pandigitals."""
    perms = it.permutations(range(1, n+1), n)
    ndigitals = [tup_concat(p) for p in perms]
    return ndigitals

def tup_concat(tup):
    """Convert a tuple of integers to a concatenated number."""
    num = ''
    for elem in tup:
        num += str(elem)
    return int(num)

#%% Construct all 2-9 digit pandigitals, reduce the list further, then check
# if prime, starting from the largest.
start = time.time()

# Construct sorted list of all 2 to 9 pandigitals.
ndigitals = []
for i in range(2, 10):
    ndigitals += get_ndigitals(i)

# Small vectorized speed boost, but the initial array conversion takes a while.
ndigitals = np.array(ndigitals)
for i in range(2, 100):  # can be optimized by iterating over primes only
    ndigitals = ndigitals[ndigitals % i != 0]
ndigitals[::-1].sort()

# Print first prime found.
for num in ndigitals:
    if is_prime(num):
        print(num)
        break

print(time.time() - start)


#%%
""" Potential improvements:
1)  All 8 and 9 digit pandigitals cannot be prime since the sum of their
    digits is divisible by 3. 

    Extensions/Remarks:
""" 
