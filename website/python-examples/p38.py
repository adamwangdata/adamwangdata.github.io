""" @author: Adam, @date: 6-23-2019 

We seek the concatenation 'm' + '2*m' + ... + 'n*m' to be pandigital, n > 1. 
The upperbound for n is 9 with lowerbound m = 1. 
The lowerbound for n is 2 with upperbound m = 9999.
"""

import time 

def is_pandigital(n, digits):
    """Check if n is pandigital, digits being the set of considered digits."""    
    if n > 10**(len(digits)) or n < 10**(len(digits) - 1):  
        return False  # too many or too few digits
    else:
        n_list = [int(i) for i in str(n)]
        n_set = set(n_list)
        return n_set == digits

def concat_prod(m, n):
    """Return concatenated product of m + 2*m + ... + n*m."""
    prod = ''
    for i in range(1, n+1):
        prod += str(m*i)
    return int(prod)

#%%  Brute force.
    
start = time.time()

# Set of digits required in pandigital.
digits = set()
for i in range(1, 10):
    digits.add(i)
    
# Try all possible concatenated products.
prods = []
for n in range(2, 10):
    for m in range(1, 10000):
        prod = concat_prod(m, n)
        if is_pandigital(prod, digits):
            prods.append(prod)
            
print(max(prods))

print(time.time() - start)


#%%
""" Potential improvements:
1)  We do not have to range through all n. Once a product is greater than
    9 digits, we know higher n will not yield a pandigital.     
    
    Extensions/Remarks:
""" 
