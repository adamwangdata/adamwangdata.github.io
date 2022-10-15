""" @author: Adam, @date: 6-13-2019 

Express two three-digit numbers in base 10:
    abc = a(10^2) + b(10^1) + c(10^0)
    def = d(10^2) + e(10^1) + f(10^0)
Their sum
    abc + def = (a+d)(10^2) + (b+e)(10^1) + (c+f)(10^0)
              = A(100) + B(10) + C.
If C >= 10, then B increases by C // 10 and the "ones" digit is C % 10.    
If (B + (C // 10))(10) >= 100, or equivalently (B + (C // 10)) >= 10, then
then A increases by (B + (C // 10)) // 10 and the "tens" digit is 
(B + (C // 10)) % 10. This logic continues as we move to larger base 10 
coefficients until the last digit where no carryover is necessary. Here
that digit is A + ((B + (C // 10)) // 10)
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

#%% Base 10 addition. 
    
start = time.time()

file = open("p13_nums.txt")
nums = file.read().split('\n')
file.close() 

total = '0'
for num in nums:
    total = big_add(total, num)
print(total)
print(total[:10])

print(time.time() - start)


#%%
""" Potential improvements:
1)  Faster way to sum multiple numbers simultaneously?
""" 
