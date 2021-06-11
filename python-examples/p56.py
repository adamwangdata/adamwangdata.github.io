""" @author: Adam, @date 7/17/2019 """

import time

#%% Brute force.  

def sum_digits(n):
    """Return sum of digits of n."""
    n_str = str(n)
    digit_sum = 0
    for char in n_str:
        digit_sum += int(char)
    return digit_sum


start = time.time()

max_sum = 1
limit = 100
for a in range(1, limit):
    for b in range(1, limit):
        digit_sum = sum_digits(a**b)
        if digit_sum > max_sum:
            max_sum = digit_sum
print(max_sum)

print(time.time() - start)


#%%
""" Potential Improvements:
    
    Extensions / Remarks:
""" 


