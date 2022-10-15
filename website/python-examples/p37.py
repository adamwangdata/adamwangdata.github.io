""" @author: Adam, @date: 6-21-2019 

An upperbound on the number of digits can be determined by finding
    min(largest right truncatable prime, largest left truncatable prime).
It turns out this is equal to the largest right truncatable prime 73939133.
This can be found in the following (very slow, ~1 hr) code:

i = 2
while True:
    # All i digit primes.
    primes = get_primes(10**i)
    primes = primes[primes >= 10**(i-1)]
    
    # Look for right truncatable primes.
    count = 0
    for prime in primes:
        if is_right_truncatable(prime):
            print(prime)
            count += 1
    
    # If none found, exit.
    if count == 0:
        break
        
    i += 1

Then, we can record all right truncatable primes from 1 to 73939133 (since
it is faster than checking left truncatable primes), and then of those check
if they are left truncatable. 
"""

import time
from p3 import is_prime
from p10 import get_primes

def is_right_truncatable(n):
    """Return true if n is a right truncatable prime."""
    # Return False if n contains an even number excluding 2.
    n_str = str(n)
    for digit in n_str:
        if int(digit) in {0, 4, 6, 8}:
            return False
 
    # Repeatedly trim from the right.
    n_len = len(n_str)
    for i in range(1, n_len):
        if not is_prime(int(n_str[:(n_len-i)])):
            return False
    else:
        return True

def is_left_truncatable(n):
    """Return true if n is a left truncatable prime."""
    # Return False if n contains 0.
    n_str = str(n)
    for digit in n_str:
        if digit == '0':
            return False
 
    # Repeatedly trim from the left.
    n_len = len(n_str)
    for i in range(1, n_len):
        if not is_prime(int(n_str[i:])):
            return False
    else:
        return True
        
#%% Mostly brute force from predetermined upper bound. Takes ~50 sec.
start = time.time()

# All primes less than up_bound and >=10.
up_bound = 73939133
primes = get_primes(up_bound)
primes = primes[primes >= 10]

# Right truncatable primes.
rt_primes = []
for prime in primes:
    if is_right_truncatable(prime):
        rt_primes.append(prime)
        
# Left and right truncatable primes.
lrt_primes = []
for prime in rt_primes:
    if is_left_truncatable(prime):
        lrt_primes.append(prime)

print(lrt_primes)
print(sum(lrt_primes))

print(time.time() - start)


#%%
""" Potential improvements:
1)  Faster prime searching algorithms will help tremendously, particularly
    for locating the upper bound.    
    
    Extensions/Remarks:
""" 

            