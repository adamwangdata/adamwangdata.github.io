""" @author: Adam, @date 7/3/2019 """

import time

#%% Brute force.

from p10 import get_primes


# Create set of primes less than n and loop through all possible consecutive
# sequences (with sum less than n). 
start = time.time()

n = int(1e6)
primes = get_primes(n)
primeset = set(primes)
n_primes = len(primes)
max_streak = 1
max_streak_prime = 2

for i in range(n_primes):
    prime_sum = 0
    streak = 0
    for j in range(i, n_primes):
        prime_sum += primes[j]
        streak += 1
        if prime_sum > n:
            break
        if prime_sum in primeset and streak >= max_streak:
            max_streak = streak
            max_streak_prime = prime_sum
print(max_streak, max_streak_prime)

print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
"""