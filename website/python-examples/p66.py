""" @author: Adam, @date 7/24/2019 

Brute force is far too slow. The largest minimal x solution has 38 digits.
Instead from Wikipedia for Pell's equation:
https://en.wikipedia.org/wiki/Pell%27s_equation
the minimal solution in x satisfies (x, y) = (num_i, den_i) for some i
where num_i/den_i is the i-th convergent. 
"""

import time 
import math

#%% Compute all minimal solutions in x for 1 <= D <= 1000 using convergents
#   of continued fraction expansions. 

def build_cfrac(n, max_iter = 100, eps = 1e-6):
    """Return continued fraction coefficients for sqrt(n). 
    Adapted from p64.py"""
    # Base case.
    m_0 = 1
    a_0 = math.floor(math.sqrt(n))
    l_0 = -a_0
    
    # Perfect square.
    if math.sqrt(n) - a_0 < eps:
        return 0
    
    # Store i = 1 to determine when a cycle is reached.
    m_1 = (n - l_0**2)/m_0
    a_1 = math.floor((math.sqrt(n) - l_0) / m_1)
    l_1 = -l_0 - a_1*(n - l_0**2)/m_0
    (m_i, a_i, l_i) = (m_1, a_1, l_1)
    coefs = [a_0, a_1]
    for i in range(max_iter):
        tmp = m_i
        
        # Update (m, a, l)
        m_i = (n - l_i**2)/m_i
        a_i = math.floor((math.sqrt(n) - l_i) / m_i)
        l_i = -l_i - a_i*(n - l_i**2)/tmp
        coefs.append(a_i)
        
    return coefs        
    
    
def nth_convergent(coefs):
    """Return n-th convergent given the first n coefficients a_i in 
    continued fraction expansion."""
    reverse_coefs = coefs[::-1]
    # Simplify fractions starting from the most-nested.
    num, den = 1, reverse_coefs[0]
    for i in range(1, len(reverse_coefs)):  
        num, den = den, reverse_coefs[i]*den + num
    num, den = den, num  # No inversion when adding last (reverse) coefficient.
    return num, den

if __name__ == '__main__':
    start = time.time()
    
    # Generate D that are not perfect squares (no solution)
    D_max = 1001
    min_xsol = []
    squares = [i**2 for i in range(1, int(D_max**.5)+1)]
    squareset = set(squares)
    D_list = [i for i in range(1, D_max) if i not in squareset]
    for D in D_list:
        max_iter = 100  # Number of convergents to try
        do_while = True
        while do_while:
            coefs = build_cfrac(D, max_iter)
            # For each convergent, check if it satisfies Pell's equation.
            for i in range(1, len(coefs)):  
                num, den = nth_convergent(coefs[:i])
                if num**2 - D*den**2 == 1:
                    min_xsol.append((num, D))
                    do_while = False
                    break
            else:  # No solution found. Increase number of convergents to check.
                print("max_iter too small")
                max_iter *= 10
    print(max(min_xsol))
    
    print(time.time() - start)

#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""