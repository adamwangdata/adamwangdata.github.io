""" @author: Adam, @date: 8-8-2019 

See scratch.pdf. """

import time 

#%% Pell's equation solution.

from p66 import build_cfrac
from p66 import nth_convergent


start_time = time.time()

p_max = int(1e9)

# Compute fundamental solution to Pell's equation with D = 3.
# Code is taken from p66.py.
D = 3
max_iter = 100  # Number of convergents to try
do_while = True
while do_while:
    coefs = build_cfrac(D, max_iter)
    # For each convergent, check if it satisfies Pell's equation.
    for i in range(1, len(coefs)):  
        num, den = nth_convergent(coefs[:i])
        if num**2 - D*den**2 == 1:
            x_1, y_1 = num, den 
            do_while = False
            break
    else:  # No solution found. Increase number of convergents to check.
        print("max_iter too small")
        max_iter *= 10

# Recursively generate other solutions from the fundamental.
x_list = [x_1]
y_list = [y_1]
k = 1
x_k, y_k = x_1, y_1
while True:
    k += 1
    x_k, y_k = x_1*x_k + D*y_1*y_k,  x_1*y_k + y_1*x_k
    if x_k > (p_max + 3 + 1) / 2:  # Resultant triangle perimeter too big.
        break
    x_list.append(x_k)
    y_list.append(y_k)

# For each Pell's equation solution, ensure two triangle lengths n and area A 
# are integers. (While x is guaranteed to be an integer, n may not be.)
# Sum triangle perimeters that meet both conditions.
p = 0
for i in range(1, len(x_list)):
    x = x_list[i]
    y = y_list[i]
    for j in [1, -1]:
        n = (2 * x + j)/3
        if int(n) == n:
            h = y
            m = n + j  # Base.
            A = m/2 * h
            if int(A) == A:
                p += m + 2*n
print(p)
print(time.time() - start_time)




#%% Brute force. Conceptually simple, but too slow.

start_time = time.time()

p_max = int(1e6)
n_max = p_max//3 + 1
squareset = {i**2 for i in range(1, n_max)}

p = 0
for n in range(2, n_max):
    for i in [-1, 1]:
        m = n + i
        h2 = n**2 - (m/2)**2  
        if h2 in squareset:
            A = m/2 * h2**.5
            if int(A) == A:
                print(n, A)
print(p)
                    
print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""


















