""" @author: Adam, @date 7/12/2019 """

import time

#%% For each n, find first binomial coefficient that exceeds 1 million.
#   Count all coefficients > 1 million using symmetry.

def fact(n):
    """Return n!"""
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod 

def n_choose_r(n, r):
    """Return binomial coefficient n choose r."""
    return fact(n) // (fact(r) * fact(n-r))

# Compute all binomial coefficients until threshold is reached.
# The number of coefficients smaller than threshold are 2*r.
start = time.time()

count = 0
thresh = int(10**6)
for n in range(1, 101):
    for r in range(0, n+1):
        if n_choose_r(n, r) > thresh:
            # Update count using symmetry.
            count += (n+1) - 2*r
            break
print(count)

print(time.time() - start)

#%%
""" Potential Improvements:
        
    Extensions / Remarks:
"""
