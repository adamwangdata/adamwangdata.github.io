""" @author: Adam, @date 6/25/2019 """


import time
import itertools as it

def tup_concat(tup):  # Modified from p41.py.
    """Convert a tuple of integers to a concatenated number string."""
    num = ''
    for elem in tup:
        num += str(elem)
    return num

#%% Construct all 0 to 9 pandigitals using one 3-sequence at a time.

start = time.time()

# Construct all possible d_2 d_3 d_4 arrangements.
perms = it.permutations(range(0, 10), 3)
base = [tup_concat(p) for p in perms]
arr = [num for num in base if int(num) % 2 == 0]

# Construct all possible larger arrangements, one digit at a time.
primes = [3, 5, 7, 11, 13, 17]
for i in range(6):
    next_arr = []
    for num in arr:
        for j in range(10):
            if str(j) not in num and int(num[-2:] + str(j)) % primes[i] == 0:
                next_arr.append(num + str(j))
    arr = next_arr

# Add d_1.
nums = []
for num in arr:
    for j in range(10):
        if str(j) not in num:
            nums.append(str(j) + num)

print(sum([int(i) for i in nums]))

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Predetermine which digits need to be checked in a string, rather than
    checking all 0, 1, ..., 9.
    
    Extensions / Remarks:
"""
