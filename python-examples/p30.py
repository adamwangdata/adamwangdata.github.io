""" @author: Adam, @date 6/19/2019

For fourth power digits, the number can be a maximum of 9^4 * 5 = 32805, 
reducing the number of cases we must check. Similarly for fifth power digits,
9^5 * 6 = 354294 is the maximum. Further restrictions can be placed on
small numbers, e.g. 9 cannot be present in any number smaller than 9^5.
"""

import time

def digit_power_sum(num, p = 5):
    total = 0
    for digit in str(num):
        total += int(digit)**p
    return total

#%% Brute force.

start = time.time()

nums = []
for num in range(2, 9**5 * 7):
    if num == digit_power_sum(num, 5):
        nums.append(num)
print(nums)
print(sum(nums))
    
print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""
      