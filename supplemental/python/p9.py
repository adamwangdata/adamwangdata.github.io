""" @author: Adam, @date: 6-12-2019 """

import time

def is_ptriplet(x, y, z):
    """Check if the numbers x, y, z can form a Pythagorean triplet."""
    plist = [x, y, z]
    plist.sort()
    return plist[0]**2 + plist[1]**2 == plist[2]**2

#%% Mostly brute force solution, scales as O(psum^2). 
    
start = time.time()
 
# Create a list of all Pythagorean triplets satisfying a + b + c = psum.
psum = 1000
triplets = []
for a in range(1, psum - 1):  # To avoid b or c = 0.
    for b in range(1, psum - a):  # To avoid c <= 0
        c = psum - a - b
        if is_ptriplet(a, b, c):
            triplets.append([a, b, c])   
            break  # avoid repeats
print(triplets)

print(time.time() - start)

""" Potential improvements: 
1)  Enforce ordering a < b < c, e.g. make first loop range from 1 to psum//3.
    This also lets us use a function like is_ptriplet() that does not sort.
    See p39.py.
"""
