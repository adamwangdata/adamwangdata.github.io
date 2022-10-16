""" @author: Adam, @date: 6-11-2019 """

import numpy as np
import time

def fibo(n):
    """Return list of all Fibonacci numbers less than n. """
    result = []
    a, b = 1, 2
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

#%% Brute force method with vectorized even check.
    
start = time.time()     

# Sum over even Fibonacci numbers less than n.
n = 4e6
fib_nums = np.array(fibo(n))
even_fib_nums = fib_nums[fib_nums % 2 == 0]
total = even_fib_nums.sum()
print(total)

print(time.time() - start)