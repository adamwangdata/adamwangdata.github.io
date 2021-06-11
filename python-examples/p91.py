""" @author: Adam, @date: 8-7-2019 

Brute force looping through all distinct points."""

import time 

#%% Solution.

def square_dist(p1, p2):
    """Return square distance given two points, each of the form (x, y)."""
    x1, x2 = p1[0], p2[0]
    y1, y2 = p1[1], p2[1]
    return (x2 - x1)**2 + (y2 - y1)**2


start_time = time.time()

limit = 50
p0 = (0, 0)

# Loop through all unique points p1 and p2, compute distances between points
# and check if they satisfy Pythagorean theorem => forms right triangle.
count = 0
i = 0
for x1 in range(limit+1):
    for y1 in range(limit+1):
        p1 = (x1, y1)
        if p1 == p0:
            continue
        
        for x2 in range(limit+1):
            for y2 in range(limit+1):
                p2 = (x2, y2)
                if p2 == p0 or p2 == p1:
                    continue
                
                # Compute distances.
                dists = [square_dist(p0, p1), 
                         square_dist(p0, p2), 
                         square_dist(p1, p2)]
                dists.sort()
                if dists[0] + dists[1] == dists[2]:  # Satisfies Pythag THM.
                    count += 1
                i += 1

print(count/2)  # Avoid double counting
                
print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
1)  Note, collinear points like p1 = (n, 0) and p2 = (m, 0) n != m, do not 
    need to be accounted for separately due to the origin p0 = (0, 0).
"""