""" @author: Adam, @date 7/2/2019 """

import time

#%% Brute force.

from p10 import get_primes

def are_permutations(n1, n2):
    """Check if n1 and n2 are permutations of each other. """
    list1 = list(str(n1))
    list2 = list(str(n2))
    
    if len(list1) != len(list2):
        return False
    
    for elem in list1:
        if elem not in list2:
            return False
        else:
            list2.remove(elem)
            
    return True


# Check all possible combinations of base numbers and increments.
# Increments must be even and base numbers must be prime.
if __name__ == '__main__':
    start = time.time()
    
    sequences = []
    n = 10000
    primes = get_primes(n)
    primeset = set(primes)
    
    for increment in range(2, n//3, 2):
        for base in primes:
            if (base > n - 2*increment):  # last term too many digits
                break
            n1 = base
            n2 = base + increment
            n3 = base + 2*increment
            if n2 in primeset and n3 in primeset:
                if are_permutations(n1, n2) and are_permutations(n1, n3):
                    seq = str(n1) + str(n2) + str(n3)
                    sequences.append(seq)        
                    
    print(sequences)
    
    print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""