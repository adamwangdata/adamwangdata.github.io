""" @author: Adam, @date 6/16/2019 """

import time

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

def is_amicable(a):
    """Check if a is an amicable number."""
    b = d(a)
    if b != a and d(b) == a:
        return True
    else: 
        return False
#%% Brute force.

start = time.time()

# For all i in 1, 2, ..., n-1, check if i is amicable. If it is, add to sum.
n = 10000
amicable_sum = 0
for i in range(1, n):
    if is_amicable(i):
        amicable_sum += i

print(amicable_sum)

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Automatically sum i's amicable pair.

    Extensions / Remarks:
"""
