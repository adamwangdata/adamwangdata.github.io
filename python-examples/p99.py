""" @author: Adam, @date: 8-10-2019 

Compare log(a^b) = b*log(a) instead, since log() is monotonic. """

import time 

#%% Extract list of (base, exp) pairs.

file = open("p99_base_exp.txt")
text = file.read()
file.close()
lines = text.split("\n")
base_exp_pairs = []
for line in lines:
    nums = line.split(",")
    base_exp_pairs.append((int(nums[0]), int(nums[1])))

#%% Compare logs.
    
import math 

def log(base, exp):
    return exp*math.log(base)


start_time = time.time()

max_line = 1
base_exp_pair = base_exp_pairs[0]
max_log = log(base_exp_pair[0], base_exp_pair[1])
n = len(base_exp_pairs)
for i in range(1, n):
    base_exp_pair = base_exp_pairs[i]
    val_log = log(base_exp_pair[0], base_exp_pair[1])
    if val_log > max_log:
        max_log = val_log
        max_line = i+1
print(max_line)        

print(time.time() - start_time)


                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""




