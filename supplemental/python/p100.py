""" @author: Adam, @date: 8-10-2019 

See scratch.pdf. """

import time 

#%% Negative Pell's equation solution.

from p66 import build_cfrac
from p66 import nth_convergent

start_time = time.time()

N_max = int(1e12)

# Compute fundamental solution to Pell's equation with D = 2.
# Code is taken from p66.py.
D = 2 
max_iter = 100  # Number of convergents to try
do_while = True
while do_while:
    coefs = build_cfrac(D, max_iter)
    # For each convergent, check if it satisfies Pell's equation.
    for i in range(1, len(coefs)):  
        num, den = nth_convergent(coefs[:i])
        if num**2 - D*den**2 == -1:
            x_1, y_1 = num, den 
            do_while = False
            break
    else:  # No solution found. Increase number of convergents to check.
        print("max_iter too small")
        max_iter *= 10

# Recursively generate other solutions from the fundamental.
x_k, y_k = x_1, y_1
while True:
    x_k, y_k = 3*x_k + 4*y_k,  2*x_k + 3*y_k
    if (x_k + 1)/2 > N_max:  
        print((y_k + 1)/2)
        break
print(time.time() - start_time)

                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""




