""" @author: Adam, @date: 6-21-2019 """

import time
from p4 import is_palindrome

def to_base2(n):
    """Convert base 10 number, n, to base 2."""
    # Determine number of digits in base 2 needed
    if n == 0:
        return 0
    
    max_exp = 0
    while True:
        if (n-1) // 2**(max_exp) == 0:
            break
        else:
            max_exp += 1
    
    # Base 2 conversion
    str_num = ''    
    for exp in range(max_exp, -1, -1):
        str_num += str(n // 2**(exp))
        n = n % 2**(exp)
    return int(str_num)
#%% Brute force.

if __name__ == '__main__':   
    start = time.time()
    
    # Find all base10 palindromes less than n.
    n = int(1e6)
    base10_palindromes = []
    for i in range(1, n):
        if is_palindrome(i):
            base10_palindromes.append(i)
    
    # Require them to be base 2 palindromes.
    base10and2_palindromes = []
    for j in base10_palindromes:
        if is_palindrome(to_base2(j)):
            base10and2_palindromes.append(j)
    
    print(sum(base10and2_palindromes))
    
    print(time.time() - start)


#%%
""" Potential improvements:
1)  Only odd numbers can be base2-palindromic.
2)  Faster base 2 conversion starting from 2^0 to 2^(max_exp).
    
    Extensions/Remarks:
""" 

            