""" @author: Adam, @date 7-29-2019

Brute force, with memoization. """

import time 

#%% Count number of digit factorial chains of length m.

def factorial(n):
    """Return n!"""
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def digit_factorial(n, factorial_dict):
    """Return sum of factorials of each digit of n."""
    n_str = str(n)
    fact_sum = 0
    for digit in n_str:
        fact_sum += factorial_dict[int(digit)]
    return fact_sum


start_time = time.time()    

# Initialize dictionary of factorials to avoid repeatedly calculating.
factorial_dict = {}
for i in range(10):
    factorial_dict[i] = factorial(i)

# Dictionary of chain lengths for a given number.
chain_len_dict = {}

n_terms = 60
count = 0
n = int(1e6)
# Compute chain lengths for all i, memoizing in dictionary as we go.
for i in range(1, n):
    
    chain_len = 0
    num = i
    chain = [num]
    # Compute chain length.
    while True:
        num = digit_factorial(num, factorial_dict)
        
        if num in chain_len_dict:  # Lookup rest of chain length.
            chain_len = len(chain) + chain_len_dict[num]
            
            # Update dictionary of chain lengths.
            k = 0
            for elem in chain:
                chain_len_dict[elem] = chain_len - k
                k += 1            
            break
        
        if num in chain:  # Repeat detected.
            chain_len = len(chain)
            
            # Update dictionary of chain lengths.
            k = 0
            for elem in chain:
                chain_len_dict[elem] = chain_len - k
                k += 1
            break
        else:  # Append chain.
            chain.append(num)

    # Update count.
    if chain_len == n_terms:
        count += 1

print(count)

print(time.time() - start_time)


#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""



    
    
    