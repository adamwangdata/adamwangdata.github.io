""" @author: Adam, @date: 8-5-2019 

Brute force. """

import time 

#%% Brute force solution.

from p10 import get_primes


start_time = time.time()

# Generate prime powers of 2, 3, and 4 less than limit.
limit = int(50e6)
p2_lim = int(limit**(1/2)) + 1
p3_lim = int(limit**(1/3)) + 1
p4_lim = int(limit**(1/4)) + 1
primeset = set(get_primes(p2_lim))
p2_nums = [i**2 for i in range(1, p2_lim+1) if i in primeset]
p3_nums = [i**3 for i in range(1, p3_lim+1) if i in primeset]
p4_nums = [i**4 for i in range(1, p4_lim+1) if i in primeset]

# Track all sums to avoid redudant counts.
sums = set()
for i4 in p4_nums:
    for i3 in p3_nums:
        for i2 in p2_nums:
            s = i2 + i3 + i4
            if s < limit:
                sums.add(s)
            else:
                break
print(len(sums))
            
print(time.time() - start_time)

#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""


                
                