""" @author: Adam, @date: 6-15-2019 

The brute force method is fairly straightforward but very inefficient. 
Starting from the top, we can't use a "greedy" approach because the entire 
path is unknown. However, on the _very last_ choice, a greedy approach is fine
because the path terminates there. Take, for example,
     3
    7 4
   2 4 6
  8 5 9 3
Conditioned on reaching the line 2 4 6, if we are at 2 we should always choose
max(8, 5) = 8 and similarly choose 9 if we are at 4 or 6. Thus the largest
sum conditioned on reaching 2 4 6 results in a reduced triangle 
     3
   7   4
 10  13  15
We can iteratively apply this logic resulting in
     3       -->  23.
  20   19
This approach will also work for Problem 67.
"""

import time

#%% Brute force method traversing all 2^rows paths.
    
start = time.time()

# Process data.
file = open("p18_tri_nums.txt")
nums = file.read().split('\n')
file.close() 
rows = len(nums)
for i in range(rows):
    nums[i] = [int(x) for x in nums[i].split(' ')]

# Compute sum over all paths.
paths = 2**(rows-1)
biggest_sum = 0
for i in range(paths):
    path_sum = nums[0][0]
    
    # Convert path number to binary with steps encoded.
    i_bin = bin(i)[2:]
    if (len(i_bin) < rows):
        i_bin = '0' * (rows - len(i_bin) - 1) + i_bin
        
    # Compute path sum.
    index = 0
    for j in range(rows - 1):
        if int(i_bin[j]):
            index += 1
            path_sum += nums[j+1][index]
        else:
            path_sum += nums[j+1][index]
    
    if path_sum > biggest_sum:
        biggest_sum = path_sum

print(biggest_sum)
            
print(time.time() - start)

#%% Bottom-up conditional approach. Used in 67.py.

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
file = open("18_tri_nums.txt")
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

#%%
""" Potential improvements:
1)  Only store length rather than full strings and don't include spaces. 
    But I prefer this "uncompressed" solution for use and ease of testing.
    
    Extensions:
1)  Trinary tree consisting of paths summing over three adjacent numbers, e.g.
            3
          2 5 1
        5 3 5 7 9
""" 
        
