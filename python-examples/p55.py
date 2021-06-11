""" @author: Adam, @date 7/17/2019 """

import time

#%% Brute force.  

def reverse(n):
    """Reverse the digits of an integer n."""
    n_str = str(n)
    return int(n_str[::-1])

def is_palindrome(n):
    """Check if integer n is a palindrome."""
    return str(n) == str(reverse(n))
    
def is_lychrel(n, max_iter=50):
    """Check if n is Lychrel, up to max_iter iterations."""
    for i in range(max_iter):
        n += reverse(n)
        if is_palindrome(n):
            return False
    return True


start = time.time()

n_max = 10000
count = 0
for n in range(1, n_max):
    if is_lychrel(n):
        count += 1
print(count)

print(time.time() - start)


#%%
""" Potential Improvements:
1)  Use memoization?
    
    Extensions / Remarks:
""" 


