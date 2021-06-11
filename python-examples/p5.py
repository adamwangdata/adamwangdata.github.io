""" @author: Adam, @date: 6-12-2019

Checking all 1, 2, ..., 20 are evenly divisible is redundant. In fact, this
problem can be solved by hand using prime factorizations. For example,
2520 = 2^3 * 3^2 * 5 * 7  (e.g. use get_prime_factors() in 3.py).
Note that all 1, 2, ..., 10 are contained:
    10 = 2 * 5
    9 = 3^2
    8 = 2^3
    7 = 7
    ... etc.
Extending to 1, 2, ..., 20,
(2^3 * 3^2 * 5 * 7) * 11 * 13 * 2 * 17 * 19 = 232792560.
"""

import time

def is_divisible(n, m):
    return n % m == 0

#%% Brute force method. 
"""This takes a while (~3 minutes). It can be shortened somewhat by first
checking 1, 2, ..., 11 with an initial guess of n = 2520, then using the
result as an initial guess to check 2, 3, ..., 12. Further improvment comes
from checking only prime factorizations of 1, 2, ..., 20, but then we may as
well use the method described above."""

start = time.time()
 
# Print smallest number evenly divisible by 1, 2, ..., m.
m = 10
n = 2
switch = 1
while switch:
    for i in range(1, m+1):
        if not is_divisible(n, i):
            break
    else:
        switch = 0
        break
    n += 2
print(n)
            
print(time.time() - start)
