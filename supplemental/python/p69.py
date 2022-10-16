""" @author: Adam, @date 7-26-2019 

Brute force using Euler's product formula. """

import time 

#%% Compute phi(n) for all n using Euler's product formula.

from p10 import get_primes
from p3 import get_prime_factors

    
start_time = time.time()

n = int(1e6) + 1
primeset = set(get_primes(n))
phi_list = []
result_list = []
for i in range(2, n):
    if i in primeset:
        phi = i - 1
    else:
        prime_factors = get_prime_factors(i)
        
        # Euler's product formula.
        phi = i
        for fact in set(prime_factors):
            phi *= (1 - 1/fact)
            
    phi_list.append(phi)
    result_list.append((i/phi, i))

print(max(result_list))

print(time.time() - start_time)



#%% Further comments.
""" Potential Improvements:
1)  See p70.py for a totient sieve.
    
    Extensions / Remarks:
"""

#%% Brute force starting from larger n; far too slow.

"""
n = int(1e6) + 1
primes = get_primes(n)
primeset = set(primes)
start_time = time.time()
prime_factors_list = []
for i in range(2, n):
    if i in primeset:
        prime_factors = [i]
    else:
        prime_factors = get_prime_factors(i) 
                
    prime_factors_list.append(prime_factors)
    
results = []
res_max = 0
for i in range(n-1, 2, -1):
    if i in primeset:
        continue
    else:
        phi = 1
        prime_factors = prime_factors_list[i-2]
        prime_factorset = set(prime_factors)
        for factors in prime_factors_list[:(i-2)]:
            for fact in factors:
                if fact in prime_factorset:
                    break
            else:
                phi += 1
            
            res = i/phi
            if res < res_max:
                break
                
    res = i/phi
    if res > res_max:
        res_max = res
        print(res_max, i)
    results.append((res, i))  
    if i % 100 == 0: print(i)
    
    
print(time.time() - start_time)
"""
    
    
    
    
    
    
    
    