""" @author: Adam, @date: 6-13-2019 """

import time

def triangular(n):
    """Return n-th triangular number."""
    return int((1+n) * (n/2))

def factors(n):
    """Return list of factors of n."""
    factors = []
    sqrt_n = int(n**.5)
    for i in range(1, sqrt_n):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    if n % sqrt_n == 0: factors.append(sqrt_n)
    return factors

#%% Brute force method. 
    
start = time.time()

# Print first triangular number with mor ethan 500 factors.
n = 0
n_factors = 1
while n_factors <= 500:
    n += 1
    m = len(factors(triangular(n)))
    if m > n_factors:
        n_factors = m
print(triangular(n))

print(time.time() - start)


#%%
""" Potential improvements:
1)  Calculate the number of factors directly without storing factors as a list.
""" 
 