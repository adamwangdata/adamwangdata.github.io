""" @author: Adam, @date: 8-9-2019 

Brute force. """

import time 

#%% Compute dictionary of divisor sums for 1, 2, ..., limit. Fairly slow.

def proper_divisors(n):
    """Return list of proper divisors of n."""
    divisors = [1]
    sqrt_n = int(n**.5)
    if sqrt_n < 2:
        return divisors
    
    for i in range(2, sqrt_n):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    if n % sqrt_n == 0: divisors.append(sqrt_n)
    return divisors


start_time = time.time()

limit = int(1e6)

# Precalculate divisor sums.
divisor_sums = {}
for n in range(1, limit):
    divisors = proper_divisors(n)
    divisor_sums[n] = sum(divisors)
print(time.time() - start_time)

#%%  Store longest chain with all elements < limit.

start_time = time.time()

# Loop through all starting points until a cyclic chain from there is found.
# Store sets of failed and successful numbers to avoid extra loops.
longest_count = 0
longest_chain = []
part_of_chains = set()
not_part_of_chains = set()
for n in range(1, limit):
    count = 0
    chain = [n]
    m = n    
    
    while True:
        m = divisor_sums[m]
        count += 1
        
        if m == n:  # Chain found, starting at n.
            chain.append(m)
            break
        elif m in chain:  # Chain found, but not starting at n.
            count = 0
            break
        elif m in part_of_chains:  # Chain already found.
            count = 0
            break
        elif m in not_part_of_chains:  # Chain already found not to exist.
            count = 0
            for elem in chain:
                not_part_of_chains.add(elem)
            break
        elif m > limit:  # Chain would have an element too big.
            count = 0
            for elem in chain:
                not_part_of_chains.add(elem)
            break
        elif m == 1:  # No chain.
            count = 0
            for elem in chain:
                not_part_of_chains.add(elem)
            break
        else:  # Assume there may still be a chain starting at n.
            chain.append(m)
        
    if count > longest_count:  # Update longest chain and count.
        longest_chain = chain
        longest_count = count
    
    if count > 0:  # Cyclic chain was found.
        for elem in chain:
            part_of_chains.add(elem)   
            
print(min(longest_chain))
print(longest_chain)
    
print(time.time() - start_time)

                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""


















