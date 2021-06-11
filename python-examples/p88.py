""" @author: Adam, @date: 8-5-2019 

Key insight: Given k, the minimal product-sum n satisfies k < n <= 2k. Thus
we only need to obtain all factor combinations of 
    m = k_min, k_min + 1, ... 2*k_max
and compute k(m) padding with ones as factors as needed. 
"""

import time 

#%% Solution.
kmax = 12000
def get_factors(n, max_factor=2*kmax):
    """Return all factor combinations, excluding the pair (1, n).
    For details see https://stackoverflow.com/a/27650555 """
    result = []
    factor = min(n // 2, max_factor)
    while factor >= 2:
        if n % factor == 0:
            divisor = n // factor
            if divisor <= factor and divisor <= max_factor:
                result.append([factor, divisor])
            result.extend([factor] + item for item in get_factors(divisor, 
                                                                  factor))
        factor -= 1
    return result

n_facts = {}
def num_prod_sum_factors(n):
    """Update n_facts dict with a list containing sizes of the set of factors
    resulting in n being a minimal product sum. """
    factors_list = get_factors(n)
    if len(factors_list) > 0:
        for factors in factors_list:
            n_ones = n - sum(factors)  # Append ones to fill rest of factors.
            n_factors = n_ones + len(factors)
            n_facts[n] = n_facts.get(n, []) + [n_factors]
    else:  # Is prime; cannot be minimal product sum.
        n_facts[n] = [0]



# Compute all factorizations for m = 2, 3, 4, ..., 2*kmax.
# For each m, map to number of factors in product sum numbers.
# For each k = 2, 3, ..., kmax, loop from k to 2k. The first m
# to have k factors is the minimal product-sum number.
start_time = time.time()

# Update n_facts dictionary containing map from m to number of factors.
for k in range(2, 2*kmax+1):
    num_prod_sum_factors(k)

# Append unique sums into res.
res = set()
for k in range(2, kmax+1):
    for i in range(k+1, 2*k+1):
        if k in n_facts[i]:
            res.add(i)
            break
print(sum(res))

print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""