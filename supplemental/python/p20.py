""" @author: Adam, @date 6/16/2019 

Recycle big_add() function from 13.py, renamed str_add()."""

import time

def str_add(x, y):
    """Return string representation of sum x+y, each represented as strings."""
    # Pad smaller string with zeros if necessary.
    if (len(x) > len(y)):
        y = '0' * (len(x) - len(y)) + y
    if (len(x) < len(y)):
        x = '0' * (len(y) - len(x)) + x
        
    # Add base by base; see discussion in opening docstring.
    digits = len(x)
    str_sum = ''
    carry_over = 0 
    for i in range(digits-1, -1, -1):
        x_digit, y_digit = int(x[i]), int(y[i])
        val = x_digit + y_digit + carry_over
        digit = val % 10
        carry_over = val // 10
        str_sum = str(digit) + str_sum
    if carry_over != 0:
        str_sum = str(carry_over) + str_sum
    return str_sum

def str_mult(x, y):
    """Return string representation of x*y, each represented as strings."""
    total = '0'
    if (len(x) > len(y)):
        for i in range(int(y)):
            total = str_add(total, x)
    else:
        for i in range(int(x)):
            total = str_add(total, y)
    return total
        
#%% Multiplication of strings using base 10 addition.

start = time.time()

# Compute n!.
n = 100
str_prod = '1'
for i in range(1, n+1):
    str_prod = str_mult(str_prod, str(i))
print(str_prod)

# Sum digits.
total = 0
for digit in str_prod:
    total += int(digit)
print(total)

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Algorithmically implement multiplication rather than using str_add()?
2)  Since Python can handle large numbers, it's fastest to calculate the
    factorial directly without the string conversion.

    Extensions / Remarks:
"""

