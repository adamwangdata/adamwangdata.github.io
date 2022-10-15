""" @author: Adam, @date 6/20/2019

Each product can only be 1-4 digits long. The smallest product with a 5 digit
number is 23456*1 is 5 digits. 
"""

import time
import itertools as it

def is_pandigital_product(a, b):
    """Check if a*b = c forms a pandigital product."""
    digits = set()
    for i in range(1, 10):
        digits.add(str(i))

    c = a * b
    digit_str = str(a) + str(b) + str(c)
    return (len(digit_str) == len(digits) and
            (set(digit_str) & digits) == digits)

def tup_to_int(tup):
    """Convert tuple (x, y, ..., z) to integer xy...z."""
    str_int = ""
    for i in tup:
        str_int += str(i)
    return int(str_int)

def subiter(tup):
    """Return list of digits (1, 2, ..., 9) with those in tuple tup removed."""
    digits = [i for i in range(1, 10)]
    for i in tup:
        digits.remove(i)
    return digits

#%% Mostly brute force.
    
start = time.time()

products = []

# All 1-4 digit permutations of (1, 2, ..., 9)
a_perms = []
for i in range(1, 5):
    a_perms += [perm for perm in it.permutations(range(1, 10), i)]

for a_perm in a_perms:
    a = tup_to_int(a_perm)
    
    # All 1-4 digit permutations of (1, 2, ..., 9) except those in a_perm.
    b_perms = []
    for i in range(1, 5):
        b_perms += [perm for perm in it.permutations(subiter(a_perm), i)]
    
    # Pandigital product check.
    for b_perm in b_perms:
        b = tup_to_int(b_perm)
        if is_pandigital_product(a, b):
            products.append(a*b)

print(sum(set(products)))

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Considerable speedup can be made by realizing a pandigital product must 
    be a product of (1 and 4) or (2 and 3) digit pairs. Thus line 39 becomes
    range(1, 3) and line 46 becomes range(3, 5).
    
    Extensions / Remarks:
"""