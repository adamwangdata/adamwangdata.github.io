""" @author: Adam, @date: 6-23-2019 """

import time 

def d_n(n):
    """Return the n-th digit of the fractional part of Champernowne's 
    constant."""
    # Determine number of digits of the number composing the n-th digit.
    i = 0
    digits = 0
    while n > digits:
        i += 1
        digits += n_digit_nums(i)
    
    # Begin with j = i-1 digit numbers.
    j = i - 1
    digits -= n_digit_nums(i)
    base = 10**j
    num = ''
    
    # Add to string, with stopping criterion based on digits.
    while len(num) + digits < n:
        num += str(base)
        base += 1
        
    return int(num[n - digits - 1])

def n_digit_nums(n):
    """Return the number of digits in all n-digit numbers."""
    return (9 * 10**(n-1)) * n

#%% Only construct the relevant part of the string for each d_n.
    
start = time.time()

# Multiply the 10^i-th element, i = 0, 1, ..., 6.
prod = 1
for j in range(1, 7):
    prod *= d_n(10**j)
print(prod)

print(time.time() - start)


#%% Brute force, with upper bound of d_(nmax). 
    
start = time.time()

# Construct string representation of Champernowne's constant.
n = int(1e6)
num = ''
i = 1
while len(num) < n:
    num += str(i)
    i += 1
    
# Multiply the 10^i-th element, i = 0, 1, ..., 6.
prod = 1
for j in range(1, 7):
#    prod *= int(num[10**j - 1])
    prod *= d_n(10**j)
print(prod)

print(time.time() - start)


#%%
""" Potential improvements:

    Extensions/Remarks:
"""  