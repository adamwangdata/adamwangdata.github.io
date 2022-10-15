""" @author: Adam, @date 7/1/2019 """

import time

#%% Brute force.

start = time.time()

power_sum = 0
for i in range(1, 1001):
    power_sum += i**i
print(str(power_sum)[-10:])

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""