""" @author: Adam, @date 7/18/2019 """

import time 
from p10 import get_primes

#%% Brute force.  

def concat(a, b):
    """Return concatenation of two numbers ab."""
    return int(str(a) + str(b))

def find_matches(compatibles, match, size):
    for elem in compatibles:
        count = 1
        match.append(elem)
        shared = list(set(compatibles) & set(prime_dicts[elem]))
        if len(shared) >= (size - count):
            print(1)

start = time.time()

# For the first n_primes primes, construct a list of primes (up to n_primes)
# it is compatible with after concatenation. 
n = 100000000
primes = get_primes(n)
primeset = set(primes)
n_primes = 5000
prime_dicts = {}
for i in range(n_primes):
    prime_dicts[i] = []
    for j in range(i+1, n_primes):
        ab = concat(primes[i], primes[j])
        ba = concat(primes[j], primes[i])
        """
        concat_max = max(ab, ba)
        if concat_max > n:  # Increase primeset.
            while concat_max > n:
                n *= 10
            print(n)
            primes = get_primes(n)
            primeset = set(primes)
        """
        if ab in primeset and ba in primeset:
            prime_dicts[i].append(j)
        
size = 5
for i in range(n_primes):
    compatibles = prime_dicts[i]
    for elem in compatibles:
        count = 2
        match = [i, elem]
        shared = list(set(compatibles) & set(prime_dicts[elem]))
        if len(shared) >= (size - count):
            for elem2 in shared:
                count = 3
                match2 = [i, elem, elem2]
                shared2 = list(set(shared) & set(prime_dicts[elem2]))
                if len(shared2) >= (size - count):
                    for elem3 in shared2:
                        count = 4
                        match3 = [i, elem, elem2, elem3]
                        shared3 = list(set(shared2) & set(prime_dicts[elem3]))
                        if len(shared3) >= (size - count):
                            print(match3, shared3)

            
print(time.time() - start)


#%%
""" Potential Improvements:
1)  Use a function recursively rather than nested for/if blocks, 
    e.g. in p61.py.
2)  Prove first found value is the minimal solution.
    
    Extensions / Remarks:
"""  


# ANS: [5, 691, 750, 867] [1050]

 











