""" @author: Adam, @date 6/18/2019 """

import time
import numpy as np

def get_proper_divisors(n):
    """Return list of proper divisors of n."""
    divisors = [1]
    sqrt_n = int(n**(.5))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if n**(.5) == sqrt_n:
        del divisors[-1]
    return divisors

def d(n):
    """Return sum of proper divisors of n."""
    return sum(get_proper_divisors(n))

def is_abundant(n):
    """Check if n is an abundant number."""
    return d(n) > n
    
def get_abundant_nums(n):
    """Return array of abundant numbers less than n."""
    # We don't need to check all numbers since all multiples of an abundant
    # number is abundant. 
    check_if_abundant = np.ones(n, dtype = bool)
    index_is_abundant = np.zeros(n, dtype = bool)
    for i in range(2, n):
        if check_if_abundant[i]:
            if is_abundant(i):
                check_if_abundant[2*i:n:i] = False
                index_is_abundant[i:n:i] = True
    abundant_nums = np.where(index_is_abundant == True)[0]
    return abundant_nums
    
#%% Mostly brute force.

start = time.time()

# Create an array and set of abundant numbers for quick look-up.
n = 28124
abundant_nums = get_abundant_nums(n)
abundant_set = set(abundant_nums)

# Sum all non abundant sums.
total = 0
for i in range(1, n):
    for num in abundant_nums:
        if (i - num) in abundant_set:  
            break
    else:  # not abundant sum
        total += i

print(total)
        

print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
1)  An alternative solution is to find all possible abundant sums less than n,
    then check membership. 
2)  Extend to non abundant triplet sums. That is, find the sum of all positive 
    integers which cannot be written as a sum of three abundant numbers.
"""
