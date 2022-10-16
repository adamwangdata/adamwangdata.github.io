""" @author: Adam, @date: 7-31-2019 

Dynamic programming. """

import time 

#%% Dynamic programming solution.

from p10 import get_primes


start_time = time.time()

max_count = 5000

n = 1000
primes = get_primes(n)

m = 1000
counts = [1] + [0] * m
for prime in primes:
    for j in range(prime, m+1):
        counts[j] += counts[j - prime]
        
    if counts[prime] > 5000:
        print(prime)
        break
    
print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
                
                
                
                
                
                
                
                
                