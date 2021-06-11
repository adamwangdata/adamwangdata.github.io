""" @author: Adam, @date 7-29-2019

The answer is a sum of totients phi(2) + phi(3) + ... + phi(d_max). If n, m
have are not relatively prime, n < m, then by definition it is reducible. """

import time 
import numpy as np

#%% Sum totients phi(2) through phi(limit).

from p70 import get_totients


start_time = time.time()    

limit = int(1e6)
totients = get_totients(limit)[1:]
print(np.sum(totients))
            
print(time.time() - start_time)


#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
"""


    
    
    
    
    