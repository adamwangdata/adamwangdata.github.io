""" @author: Adam, @date 7-29-2019

Mostly brute force. """

import time 

#%%  

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)


start_time = time.time()    

limit = int(12000)
target1 = 1/3
target2 = 1/2
count = 0

# For each n, quickly find d so that n/d is as close as possible to and 
# larger than target1. We don't need to loop through large n such that
# n/d > target for all d. Then count fractions greater until n/d >= target2.
for n in range(1, int(limit*target2)+1):
    
    # Continuously halve d.
    d = limit
    half_counter = 0
    while n/d < target1:
        d = d // 2
        half_counter += 1
    if half_counter > 0: 
        d *= 2
    
    # Increment, halving increment size if overshoot.
    inc = (d - d//2) // 2
    while inc > 1:
        d += -inc
        if n/d < target1:
            continue
        else:
            d += inc
            inc = inc // 2
    
    # Finish incrementing by one.                    
    while n/d <= target1:
        d += -1

    # Loop through and count larger fractions until greater than target2.
    d_start = d
    for d in range(d_start, n, -1):
        if n/d >= target2: 
            break
        if gcf(n, d) == 1:
            count += 1
            
print(count)
            
print(time.time() - start_time)


#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""


    
    
    
    
    