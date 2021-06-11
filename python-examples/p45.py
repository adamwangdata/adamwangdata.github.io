""" @author: Adam, @date 6/25/2019 """

import time

def T(n):
    """Return n-th triangle number."""
    return n*(n+1) // 2

def grow_tris(tris, n):
    """Extend list of triangle numbers to include n."""
    i = len(tris) + 1
    while tris[-1] < n:
        tris.append(T(i))
        i += 1
    return tris

def P(n):
    """Return n-th pentagonal number."""
    return n*(3*n-1) // 2

def grow_pents(pents, n):
    """Extend list of pentagonal numbers to include n."""
    i = len(pents) + 1
    while pents[-1] < n:
        pents.append(P(i))
        i += 1
    return pents

def H(n):
    """Return n-th hexagonal number."""
    return n*(2*n-1) 

def grow_hexs(hexs, n):
    """Extend list of hexagonal numbers to include n."""
    i = len(hexs) + 1
    while hexs[-1] < n:
        hexs.append(H(i))
        i += 1
    return hexs


#%% Brute force, but slow. See below, and potential improvements.

start = time.time()

tri_nums = [1]
pent_nums = [1]
hex_nums = [1]   
n = 285
while True:
    n += 1
    t_n = T(n)
    pent_nums = grow_pents(pent_nums, t_n)
    hex_nums = grow_hexs(hex_nums, t_n)
    
    if t_n in pent_nums and t_n in hex_nums:
        print(n, t_n)
        break
        
print(time.time() - start)

#%% Create smaller lists using analytic methods.
def get_pents(p1, p2):
    n = int((1 + (1+24*p1)**.5) / 6)
    pents = []
    while True:
        p_n = P(n)
        pents.append(p_n)
        n += 1
        if p_n > p2:
            break
    return pents

def get_hexs(h1, h2):
    n = int((1 + (1+8*h1)**.5) / 4)
    hexs = []
    while True:
        h_n = H(n)
        hexs.append(h_n)
        n += 1
        if h_n > h2:
            break
    return hexs
    
start = time.time()

tri_nums = [1]
pent_nums = [1]
hex_nums = [1]   
n = 285
while True:
    n += 1
    t_n = T(n)
    t_i = T(n-1)
    pent_nums = get_pents(t_i, t_n)
    hex_nums = get_hexs(t_i, t_n)
    
    if t_n in pent_nums and t_n in hex_nums:
        print(n, t_n)
        break

print(time.time() - start)

#%%
""" Potential Improvements:
1)  All hexagonal numbers are triangle numbers, so triangle numbers can be
    ignored. 
2)  Analytic methods, e.g. P = n(3n-1)/2) implies n = (1 + sqrt(1 + 24P))/6.

    Extensions / Remarks:
"""