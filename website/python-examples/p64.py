""" @author: Adam, @date 7/23/2019 

See scratch.pdf for notes."""

import time 
import math

#%% Count number of sqrt(n) continued fractions with odd periods. 

def build_cfrac(n, max_iter = 100, eps = 1e-6):
    """Return continued fraction period for sqrt(n)."""
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
    period = 0
    for i in range(max_iter):
        period += 1
        tmp = m_i
        
        # Update (m, a, l)
        m_i = (n - l_i**2)/m_i
        a_i = math.floor((math.sqrt(n) - l_i) / m_i)
        l_i = -l_i - a_i*(n - l_i**2)/tmp
        
        # Check if cycle reached.
        if (m_i, a_i, l_i) == (m_1, a_1, l_1):
            return period
            
    print('period > max_iter')
    
    
start = time.time()

count = 0
for i in range(10001):
    period = build_cfrac(i, max_iter = 1000)
    if period % 2 == 1:
        count += 1
print(count)

print(time.time() - start)    

#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
1)  See below for (perhaps) more straightforward algorithms that run
    into precision / big number problems.
"""
#%% Algorithms with issues. 

def build_cfrac(n, max_iter = 100, eps = 1e-6):
    """num and den too big after many iterations."""
    a = math.floor(math.sqrt(n))
    num = math.sqrt(n) - a
    den = 1
    base_frac = num/den
    if base_frac < eps:
        return 0
    
    period = 0
    n1 = 1
    n2 = a
    for i in range(max_iter):
        period += 1
        
        n3 = n1 * (math.sqrt(n) + n2)
        n4 = n - n2**2
        b = math.floor(n3/n4)
        
        num = n3 - b*n4
        den = n4
        frac = num/den
        
        n1 = den 
        n2 = math.sqrt(n) - num
        
        if (frac - eps < base_frac and frac + eps > base_frac):
            return period
        
    print('period > max_iter')

def build_cfrac(n, max_iter = 100, eps = 1e-6):
    """Not precise enough after many iterations."""
    a0 = math.floor(math.sqrt(n))
    base_frac = math.sqrt(n) - a0
    if base_frac < eps:
        return 0
    
    period = 1
    frac = base_frac
    for i in range(max_iter):
        coef = math.floor(1/frac)
        frac = 1/frac - coef
        
        if (frac - eps < base_frac and frac + eps > base_frac):
            return period
        
        period += 1
        
    print('period > max_iter')

            
            
            
