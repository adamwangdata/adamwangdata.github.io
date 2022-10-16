""" @author: Adam, @date 6/19/2019 

Make use of long division. long_div() is not used, but is a useful guide
(and logic check).
"""

import time

def long_div(a, b, n = 10):
    """Perform long division of a/b up to n digits."""
    result = []
    while a < b:
        result.append(0)
        a = a * 10
        
    for i in range(n):
        result.append(a // b)
        a = (a % b) * 10

    return result

def cycle_len(a, b):
    """Return the cycle length of a/b."""
    while a < b:
        a = a * 10
        
    cycle_len = 0
    count = 0
    remainders = []
    while True:
        a = (a % b) * 10
        rem = a % b
        if rem == 0:  # No cycle.
            cycle_len = 0
            break
        elif rem in remainders:  # Cycle.
            cycle_len = count - remainders.index(rem)
            break
        else:  # Continue looking for bigger cycle.
            count += 1
        remainders.append(rem)
        
    return cycle_len
            

#%% Long division brute force.

start = time.time()

# Compute cycle lengths of 1/d for d = 2, 3, ..., n-1.
n = 1000
cycle_lengths = [0, 0]
for i in range(2, n):
    cycle_lengths.append(cycle_len(1, i))    
    
print(cycle_lengths.index(max(cycle_lengths)), 
      "has cycle length", max(cycle_lengths))

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""
        
        
        
        
        
        
        