""" @author: Adam, @date 7/24/2019 """

import time 
import math

#%% Generate coefficients, then repeatedly simplify to obtain n-th convergent.

def cfrac_e_coefs(n):
    """Return list of the first n coefficients in the (infinite) continued 
    fraction of e = [2; 1, 2, 1, 1, 4, 1, ..., 1, 2k, 1, ...]"""
    coefs = [2]
    k = 1
    for i in range(1, n):
        if i % 3 == 0 or i % 3 == 1:
            coefs.append(1)
        else:
            coefs.append(2*k)
            k += 1
    return coefs

def convergent(coefs):
    """Return n-th convergent of e, where n = len(coefs). """
    reverse_coefs = coefs[::-1]
    # Simplify fractions starting from the most-nested.
    num, den = 1, reverse_coefs[0]
    for i in range(1, len(reverse_coefs)):  
        num, den = den, reverse_coefs[i]*den + num
    num, den = den, num  # No inversion when adding last (reverse) coefficient.
    return num, den
    
    
start = time.time()

n = 100
coefs = cfrac_e_coefs(n)
num, den = convergent(coefs)
digit_sum = 0
for elem in str(num):
    digit_sum += int(elem)
print(digit_sum)

print(time.time() - start)

#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
1)  I tried to generate a list of coefficients for any irrational n, but ran 
    into floating point issues after a few coefficients. See function below,
    and scratch.pdf for details.
"""
#%% Algorithms with issues. 

def cfrac_coefs(x, max_iter = 100):
    """Return continued fraction coefficients for n. Adapted from p64."""
    # Base case.
    a_0 = math.floor(x)
    k_0 = 1
    l_0 = -a_0
    m_0 = 0
    n_0 = 1
    
    a_1 = math.floor((m_0*x + n_0)/(k_0*x + l_0))
    k_1 = (m_0 - a_1*k_0)
    l_1 = n_0 - a_1*l_0
    m_1 = k_0
    n_1 = l_0
    (a_i, k_i, l_i, m_i, n_i) = (a_1, k_1, l_1, m_1, n_1)
    coefs = [a_0, a_1]
    for i in range(max_iter):
        tmp_a, tmp_k, tmp_l, tmp_m, tmp_n = a_i, k_i, l_i, m_i, n_i
        print(a_i, k_i, l_i, m_i, n_i)
        a_i = math.floor((tmp_m*x + tmp_n) / (tmp_k*x + tmp_l))
        k_i = tmp_m - a_i*tmp_k
        l_i = tmp_n - a_i*tmp_l
        m_i = tmp_k
        n_i = tmp_l
        
        coefs.append(a_i)
    
    return coefs
            
            
            
