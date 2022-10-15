""" @author: Adam, @date: 8-4-2019 

Reduce number of loops by counting combinations. """

import time 

#%% Counting solution.

def count_combinations(n, M):
    """Count number of combinations of (a, b) such that a + b = n,
    0 < a, b <= M. """
    if n <= M + 1:
        return n // 2 
    else:
        if n % 2 == 0:
            return M - n // 2 + 1  # + 1 due to (n/2, n/2) combination
        else:
            return M - n // 2
    

start_time = time.time()

limit = int(1e6)

# Pre-generate set of squares to check integer length solutions. 
i_max = int(1e5)
squares = {i**2 for i in range(1, i_max)}
count = 0
M = 0
# For each M (hypotenuse), loop through all side lengths a, b such that
# sqrt(M^2 + (a+b)^2), the shortest path, has integer length. For each
# a+b, count number of cuboids have the same shortest length.
while True:
    M += 1
    for n in range(2, 2*M+1):
        if (M**2 + n**2) in squares:
            count += count_combinations(n, M)
    if count > limit:
        break
print(M)
    
print(time.time() - start_time)

#%% Comments.
""" Potential improvements:
1)  Increase size of squares as necessary. Something like:
    if (m**2 + n**2) > max(squares):
        inc squares up to (m**2 + n**2)
    
    Extensions/Remarks:
"""

#%% Brute force solution. Simple, but too slow.

def get_shortest_path(l, w, h):
    sorted_dim = sorted([l, w, h])
    return (sorted_dim[2]**2 + (sorted_dim[0] + sorted_dim[1])**2)**.5

start_time = time.time()

M = 10
count = 0
for i in range(1, M+1):
    for j in range(i, M+1):
        for k in range(j, M+1):
            dist = get_shortest_path(i, j, k)
            if int(dist) == dist:
                count += 1
                print(i, j, k)

print(time.time() - start_time)




                
                
                