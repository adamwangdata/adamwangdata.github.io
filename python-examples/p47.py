""" @author: Adam, @date 7/1/2019 """

import time

#%% Brute force with no hard-coded upper bounds.

from p3 import is_prime
from p3 import get_prime_factors

# Keep a counter that increments if there are n_fac unique factors.
start = time.time()

n_fac = 4
counter = 0
i = 1
while counter < n_fac:
    i += 1
    if not is_prime(i) and len(set(get_prime_factors(i))) == n_fac:
        counter += 1
    else:
        counter = 0
print(i - (n_fac-1))

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Pregenerate primes using a Sieve and do not iterate over them. 
    
    Extensions / Remarks:
"""