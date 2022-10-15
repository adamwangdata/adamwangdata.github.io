""" @author: Adam, @date 7-29-2019

Mostly brute force. """

import time 

#%% Find maximum fraction n/m < target closest to target for d <= 10**6.

def gcf(a, b):
    """Return greatest common factor of a and b."""
    if b == 0:
        return a
    return gcf(b, a % b)


start_time = time.time()    

limit = int(1e6)
target = 3/7
fracs = []

# For each n, quickly find d so that n/d is as close as possible to and 
# smaller than target. We don't need to loop through large n such that
# n/d > target for all d.
for n in range(1, int(limit*target)+1):
    
    # Continuously halve d.
    d = limit
    half_counter = 0
    while n/d < target:
        d = d // 2
        half_counter += 1
    if half_counter > 0: 
        d *= 2

    # Increment, halving increment size if overshoot.
    inc = (d - d//2) // 2
    while inc > 1:
        d += -inc
        if n/d < target:
            continue
        else:
            d += inc
            inc = inc // 2
            
    # Finish incrementing by one.        
    while n/d < target:
        d += -1
    d += 1
    
    if gcf(n, d) == 1:
        fracs.append((n/d, n, d))
            
print(max(fracs))
            
print(time.time() - start_time)


#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""
    
    
    
    
    