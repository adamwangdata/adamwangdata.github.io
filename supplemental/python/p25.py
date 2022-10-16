""" @author: Adam, @date 6/19/2019 

Recycle big_add() function from 13.py.
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

def big_fib(n):
    """Return largest n-digit Fibonacci number and its index."""
    b_index = 2
    a, b = '1', '1'
    while len(b) < n:
        a, b = b, big_add(a, b)
        b_index += 1
    return a, b_index - 1
    
#%% Mostly brute force.

start = time.time()

print(big_fib(999)[1] + 1)

print(time.time() - start)

#%%
""" Potential Improvements:
1)  Since Python handles big numbers, this is far more efficient:
    def fib(n):
        b_index = 2
        a, b = 1, 1
        while len(str(b)) < n:
            a, b = b, a+b
            b_index += 1
        return a, b_index - 1
        
    Extensions / Remarks:
1)  Given a permutation, what is its order? See order() function below.
"""
        
        
        
        
        
        
        