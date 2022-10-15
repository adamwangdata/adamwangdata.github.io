""" @author: Adam, @date: 6-21-2019 """

import time
from p10 import get_primes

def get_rotations(n):
    """Return all unique rotations of n."""
    rotations = []
    for i in range(len(str(n))):
        n = rotate(n)
        rotations.append(int(n))
    return list(set(rotations))
    
def rotate(n):
    """Rotate the digits an integer clockwise. """
    n = str(n)
    if len(n) == 1:
        return n
    else:
        return n[1:] + n[0]

def get_circular_primes(primes):
    """Return list of circular primes given a list or array of primes."""
    primes_set = set(primes)  # For fast membership lookup
    circular_primes = []
    for prime in primes:
        # Append if prime is a circular prime.
        rotations = get_rotations(prime)
        for r in rotations:
            if r not in primes_set:
                break
        else:
            circular_primes.append(prime)
    return circular_primes

def remove_even_digits(nums):
    """Remove all numbers with an even digit."""
    evens = {0, 2, 4, 6, 8}
    odd_nums = []
    for num in nums:
        for digit in str(num):
            if int(digit) in evens:
                break
        else:
            odd_nums.append(num)
    return odd_nums

#%% Compute primes < n consisting of odd digits, then get circular primes < n.
    
start = time.time()

n = int(1e6)
primes = get_primes(n)
odd_primes = remove_even_digits(primes)
circular_primes = get_circular_primes(odd_primes)
print(len(circular_primes) + 1)  # 2 is an even prime!

print(time.time() - start)


#%%
""" Potential improvements:
1)  Reduce redundant calculations. For example, if 13 is a circular prime,
    then 31 must be as well.
    
    Extensions/Remarks:
""" 

            