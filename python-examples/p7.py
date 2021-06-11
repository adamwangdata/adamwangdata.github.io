""" @author: Adam, @date: 6-12-2019 

I recycle my is_prime() function from 3.py.
"""

import time

def is_prime(n):
    """Return True if n is prime and False otherwise."""
    for i in range(2, int(n**(.5)) + 1):  # int() takes the floor for us
        if n % i == 0:
            return False
    return True

#%% Mostly brute force solution. 
    
start = time.time()
 
# Print the m-th prime number.
count = 1  # Include 2, the only even prime.
n = 1
m = 10001
while count < m:
    n += 2  # Don't need to check even numbers.
    if is_prime(n):
        count += 1
print(n)
            
print(time.time() - start)
