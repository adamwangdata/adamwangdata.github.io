""" @author: Adam, @date 6/25/2019 """

import time
import math

def P(n):
    """Return n-th pentagonal number."""
    return n*(3*n-1) // 2

def grow_pents(pents, n):
    """Extend list of pentagonal numbers to include n."""
    i = len(pents) + 1
    while pents[-1] < n:
        pents.append(P(i))
        i += 1
    return pents

def S(a, b):
    return a + b

def D(a, b):
    return abs(a - b)

#%% Brute force, and incredibly slow. It turns out the first d_min found
# is the solution, but it takes some math to speed this algorithm up.

start = time.time()

# Continuously increase the size of our list of pentagonal numbers such that
# the sum of the two biggest pentagonal numbers is contained. Check each pair
# once of numbers once. We have found the minimum once the smallest possible
# difference we have not checked is larger than the current minimum.
n = 1
d_min = math.inf
pent_nums = [1]
while True:
    n += 1
    p_n = P(n)
    pent_nums = grow_pents(pent_nums, S(p_n, pent_nums[-1]))
    pent_nums_set = set(pent_nums)
    for i in range(n - 1):
        p_i = pent_nums[i]
        if (S(p_n, p_i) in pent_nums_set) and (D(p_n, p_i) in pent_nums_set):
            d_i = D(p_n, p_i)
            if d_i < d_min:
                d_min = d_i
            print(n, p_n, d_min)
            break

    if d_min < D(P(n+1), p_n):
        break
        

print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
"""