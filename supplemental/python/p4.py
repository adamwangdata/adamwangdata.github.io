""" @author: Adam, @date: 6-11-2019 """

import time

def is_palindrome(n):
    """Determine whether the integer n is a palindrome."""
    n_str = str(n)
    for i in range(len(n_str) // 2):
        if n_str[i] != n_str[-(i+1)]:
            return False
    return True
        
#%% Brute force method.
    
if __name__ == '__main__':
    start = time.time()
     
    # Print maximum of list of palindromes that are products of 3-digit numbers.
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j):
                palindromes.append(i*j)
    print(max(palindromes))
                
    print(time.time() - start)