""" @author: Adam, @date: 6-13-2019 """

import time
from p3 import get_prime_factors

def is_curious_frac(a, b):
    """Check if a/b, b > a, is a curious fraction."""
    # Convert integer to list of string digits
    a_list = [char for char in str(a)]
    b_list = [char for char in str(b)]
    
    # Compute set intersection and remove shared digits
    shared = list(set(a_list) & set(b_list))
    n = len(shared)
    if n > 0 and n < min(len(a_list), len(b_list)):
        for i in range(n):
            a_list.remove(shared[i])
            b_list.remove(shared[i])
    else:
        return False
    
    # Compare canceled fraction to original
    a_reduced = int(''.join(a_list))    
    b_reduced = int(''.join(b_list))    
    return a_reduced/b_reduced == a/b

#%% Check all valid num/den fractions.
    
start = time.time()

fracs = []
nums = [x for x in range(11, 100) if ('0' not in str(x))]  # ignore zeros
n = len(nums)
for i in range(n):
    num = nums[i]
    for j in range(i+1, n):  # j > i
        den = nums[j]
        if is_curious_frac(num, den):
            fracs.append((num, den))
print(fracs)

# Multiply found fractions together
num, den = 1, 1
for frac in fracs:
    num *= frac[0]
    den *= frac[1]
     
# Simplify by using prime factorization
num_facs = get_prime_factors(num)
den_facs = get_prime_factors(den)
num_reduced = 1
den_reduced = 1
for den_fac in den_facs:
    if den_fac in num_facs:
        num_facs.remove(den_fac)
    else:
        den_reduced *= den_fac
for num_fac in num_facs:
    num_reduced *= num_fac
print(num_reduced, '/', den_reduced)

print(time.time() - start)


#%%
""" Potential improvements:
    
    Extensions/Remarks:
1)  Extend to 3+ digit numeractor/denominators. My code as is only results in
    cancellations of the first found shared digits.
""" 
            