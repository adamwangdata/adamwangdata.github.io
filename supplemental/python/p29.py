""" @author: Adam, @date 6/19/2019 """

import time

#%% Sum over odd squares (and related corners).

start = time.time()

nums = []
for a in range(2, 101):
    for b in range(2, 101):
        nums.append(a**b)
print(len(set(nums)))

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""
        
        
        
        
        
        