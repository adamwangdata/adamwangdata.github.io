""" @author: Adam, @date 7/17/2019 

See scratch.pdf for notes. """

import time

#%% Brute force.  

def num_digits(n):
    """Return number of digits in n."""
    return len(str(n))


start = time.time()

count = 0
# Base fraction is 1 + 1/2
num = 1
den = 2
for i in range(999):
    num, den = den, 2*den + num  # Update fractional part
    if num_digits(den + num) > num_digits(den):
        count += 1
print(count)

print(time.time() - start)


#%%
""" Potential Improvements:
    
    Extensions / Remarks:
""" 


