""" @author: Adam, @date 7/3/2019 """

import time

#%% Brute force.

from p10 import get_primes
import itertools as it

def get_family_struc(n_digits, comb, base_num):
    """Return family structure given number of digits, positions of 
    wildcard digits, and values of remaining digits. 
    
    Example: n_digits = 5, comb = (3, 4), base_num = 563 
        yields structure [5, 6, *, *, 3]."""
    base_num_list = [int(char) for char in str(base_num)]
    num_list = []
    for digit_place in range(1, n_digits + 1):
        if digit_place in wild_comb:
            num_list.append('*')
        else:
            num_list.append(base_num_list.pop(0))
    return num_list

def count_primes(struc, primeset):
    """Count the number of primes in the family given its structure
    and a set of primes."""
    wild_comb = [i+1 for i in range(len(struc)) if struc[i] == '*']
    n_primes = 0
    struc_copy = struc[:]
    # Loop through all wildcard possibilities.
    for j in range(0, 10):
        for digit in wild_comb:
            struc_copy[digit - 1] = j
        num_str = ''
        for elem in struc_copy:
            num_str += str(elem)
        if int(num_str) in primeset and num_str[0] != '0':
            n_primes += 1
    return n_primes


# Check all possible families up to max_n_digits and print matches.
start = time.time()

max_n_digits = 7
n_primes_target = 8
n = int(10**(max_n_digits))
primes = get_primes(n)
primeset = set(primes)

for n_digits in range(2, max_n_digits):
    for n_replace in range(1, n_digits):  # Number of wildcard digits.
        # All combinations of n_replace wildcard digit positions.
        if n_primes_target > 5:  # Don't include last digit (5 evens).
            wild_combs = it.combinations(range(1, n_digits), n_replace)
        else:
            wild_combs = it.combinations(range(1, n_digits+1), n_replace)

        # For each set of wildcard combinations, check all families.
        for wild_comb in wild_combs:
            n_wild_digits = len(wild_comb)
            n_base_digits = n_digits - n_wild_digits
            for base_num in range(10**(n_base_digits - 1), 
                                  10**(n_base_digits)):
                if base_num % 2 == 0:  # Cannot be even.
                    continue
                
                # Count primes in family.
                num_list = get_family_struc(n_digits, wild_comb, base_num)
                n_primes = count_primes(num_list, primeset)
                if n_primes == n_primes_target:
                    print(num_list)


print(time.time() - start)

#%%
""" Potential Improvements:
1)  Instead of checking prime membership for all families up to max_n_digits,
    restrict families to those in primes.
        
    Extensions / Remarks:
"""
