""" @author: Adam, @date: 7-31-2019 

Python decimal library to the rescue. """

import time 
import decimal

#%% Brute force solution with decimal module.

def decimal_sum(n, precision):
    """Return sum of first (precision-2) digits (including before the
    decimal point)."""
    sqrt_str = str(decimal.Decimal(n).sqrt())
    total = int(sqrt_str[0])
    for char in sqrt_str[2:-2]:
        total += int(char)
    return total


start_time = time.time()

precision = 102
decimal.getcontext().prec = precision
squares = [i**2 for i in range(1, 10)]
digital_sum = 0
for i in range(1, 100):
    if i in squares:
        continue
    else:
        digital_sum += decimal_sum(i, precision)
print(digital_sum)

print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
1)  Can be solved without decimal library using long division.
""" 
                
                
                
                
                
                
                
                
                
                
                