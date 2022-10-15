""" @author: Adam, @date 7/12/2019 """

import time

#%% Brute force.

def is_permutation(a, b):
    """Return True if numbers a and b contain exactly the same digits."""
    a_list = list(str(a))
    b_list = list(str(b))
    for elem in b_list:
        if elem not in a_list:
            return False
        else:
            a_list.remove(elem)
    return True

# Check all numbers up to (10^digits)//6 for digits = 2, 3, ...
start = time.time() 

digits = 2
do_search = True
while do_search:
    base = 10**(digits - 1)
    for i in range(base, base*10//6 + 1):
        for j in range(2, 7):
            if not is_permutation(i, i*j):
                break
        else:
            print(i)
            do_search = False
            break
    digits += 1

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""
