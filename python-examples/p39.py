""" @author: Adam, @date: 6-23-2019 """

import time 

def is_ptriplet(a, b, c):
    """Check a, b, c where a <= b <= c form a Pythagorean triplet."""
    return a**2 + b**2 == c**2

#%% Brute force, looping through all distinct orderings a <= b <= c.
    
start = time.time()

max_sol = (0, 0)  # (number of triangles, perimeter)
for p in range(1, 1001):
    triplets = []
    for a in range(1, p//2 + 2):  # Max length = p/2 (triangle inequality).
        for b in range(a, p//2 + 2):  # b >= a
            c = p - a - b
            if c < b:  # c >= b
                break
            
            if c < a + b and is_ptriplet(a, b, c):  # Triangle inequality.
                triplets.append((a, b, c))
                
    if len(triplets) > max_sol[0]:  # Update.
        max_sol = (len(triplets), p)
        
print(max_sol)

print(time.time() - start)


#%%
""" Potential improvements:
1)  Rather than computing all triplets for a given perimeter, we can compute
    all perimeters for a given triplet. This reduces the number of
    redundant calculations needed.     
    
    Extensions/Remarks:
""" 
