""" @author: Adam, @date: 7-30-2019 

Euclid's formula to generate unique Pythagorean triples.  """

import time 

#%% Solution.

def gcf(a, b):
    """Return greatest common factor of a and b."""
    if b == 0:
        return a
    return gcf(b, a % b)


start_time = time.time()

L = int(1.5e6)
# To determine upperbounds on {(m, n) | m > n}, note c = k(m^2 + n^2)
# is minimized with k = n = 1, thus min_m(c) = m^2 + 1. An
# upperbound is therefore m^2 + 1 < L/2. 
n_max = m_max = int((L/2)**.5)  # c = k(m^2 + n^2)
perimeter_dict_count = {}

# Generate all primitive triples and their multiples with perimeter p < l.
for n in range(1, n_max):
    for m in range(n + 1, m_max):
        
        # Ensure unique primitive triples.
        if (n % 2 == 1 and m % 2 == 1) or gcf(n, m) != 1:
            continue
        
        # Generate multiples with p < L.
        k = 1
        a = k * (m**2 - n**2)
        b = k * (2*m*n)
        c = k * (m**2 + n**2)
        p = a + b + c
        while p < L:
            perimeter_dict_count[p] = perimeter_dict_count.get(p, 0) + 1
            k += 1
            a = k * (m**2 - n**2)
            b = k * (2*m*n)
            c = k * (m**2 + n**2)
            p = a + b + c
            
        if k == 1:  # p will continue exceeding L.
            break
        
# Count singular iteger right triangles.
count = 0
for k, v in perimeter_dict_count.items():
    if v == 1:
        count += 1
print(count)                            
    
print(time.time() - start_time)
                
                
                

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
                
                
                
                
                
                
                
                
                