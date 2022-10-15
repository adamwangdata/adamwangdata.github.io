""" @author: Adam, @date: 6-14-2019 

Recycle my big_add() function from 13.py noting that raising by an additional
power of two doubles. 
"""

import time

def big_add(x, y):
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

def double(x):
    """Return twice string reprentation of x."""
    return big_add(x, x)

#%% Base 10 addition to double.
    
start = time.time()

# Compute 2^n
n = 1000
str_num = '1'
for i in range(n):
    str_num = double(str_num)
# Sum digits
digit_sum = 0
for digit in str_num:
    digit_sum += int(digit)
print(digit_sum)

print(time.time() - start)


#%%
""" Potential improvements:
1)  Python can handle big numbers easily (but I assumed it couldn't above), 
    so the easiest solutions is 
        str_num = str(2**(1000))
    then sum the digits.
""" 
