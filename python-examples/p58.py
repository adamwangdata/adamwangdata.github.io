""" @author: Adam, @date 7/17/2019 """

import time
from p3 import is_prime

#%% Brute force.  
 
# Expand spiral and check if four diagonals are prime each expansion. Continue
# until ratio of primes to diagonals is less than 0.1.
start = time.time()

length = 3
n = length**2  # Largest diagonal.
n_diag = length*2 - 1
n_primes = 3
while n_primes / n_diag >= .1:
    length += 2
    n = length**2
    n_diag = length*2 - 1
    for i in range(4):
        if is_prime(n - (length-1)*i):
            n_primes += 1
print(length, n_primes / n_diag)

print(time.time() - start)


#%%
""" Potential Improvements:
    
    Extensions / Remarks:
""" 


