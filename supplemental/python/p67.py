""" @author: Adam, @date: 6-15-2019 

Code recycled from 18.py; see 18.py for additional details. 
"""

import time

#%% Bottom-up conditional approach. 

def reduce_triangle(nums):
    last_row = nums[-1]
    next_last_row = nums[-2]
    for i in range(len(next_last_row)):
        next_last_row[i] += max(last_row[i], last_row[i+1])
    nums = nums[:-2]
    nums.append(next_last_row)
    return nums
   
start = time.time()

# Process data.
file = open("p67_tri_nums.txt")
nums = file.read().split('\n')
file.close() 
rows = len(nums)
for i in range(rows):
    nums[i] = [int(x) for x in nums[i].split(' ')]

# Compute maximum path sum.
while len(nums) > 1:
    nums = reduce_triangle(nums)
print(nums)
            
print(time.time() - start)

