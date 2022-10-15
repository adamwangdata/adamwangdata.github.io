""" @author: Adam, @date: 8-9-2019 

Multiply a*b, keeping track of last 10 digits. """

import time 

#%% 

def big_mult(a, b, n):
    """Multiply two numbers together, accurate up to the last n digits. """
    a = int(str(a)[-n:])
    b = int(str(b)[-n:])
    return int(str(a*b)[-n:])

start_time = time.time()

# Continuously multiply 2^exp_inc
exponent = 7830457
exp_inc = 100
n_digits = 10
n = 28433
digits = 2**exp_inc
while True:
    exponent -= exp_inc
    if exponent < exp_inc:
        break
    digits = big_mult(digits, 2**exp_inc, n_digits)

# Finish multiplying by 2
for i in range(exponent):
    digits = big_mult(digits, 2, n_digits)

# Multiply by n and add one.
digits = big_mult(digits, n, n_digits) + 1
print(digits)

print(time.time() - start_time)


                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""

#%% Brute force using modular arithemtic.

start_time = time.time()

exponent = 7830457
n_digits = 10
mod_by = 10**n_digits
n = 28433
digits = 1
for i in range(exponent):
    digits = (digits * 2) % mod_by
digits = digits * n % mod_by
digits += 1

print(digits)
print(time.time() - start_time)















