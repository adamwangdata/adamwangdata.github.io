""" @author: Adam, @date: 6-20-2019 

A conservative upperbound is 9! * 7 = 2,540,160. The first digit is a 2, so
we further reduce to 2! + 9!*6 = 2,177,282."""

import time

def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

def is_curious(n, fact_dic):
    """Check if n is curious, given a factorial dictionary mapping i to i! for
    i = 0, 1, ..., 9."""
    list_n = [int(char) for char in str(n)]
    total = 0
    for i in list_n:
        total += fact_dic[i]
    return n == total

#%% Brute force with memoized factorial dictionary.
    
start = time.time()

# Memoize repeated factorial calculations.
fact_dic = {}
for i in range(0, 10):
    fact_dic[i] = factorial(i)
    
# Find curious numbers.
n_curious = []
for i in range(10, factorial(9)*6 + factorial(2)):
    if is_curious(i, fact_dic):
        n_curious.append(i)
print(n_curious)
print(sum(n_curious))

print(time.time() - start)


#%%
""" Potential improvements:
    
    Extensions/Remarks:
""" 

            