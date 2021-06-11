""" @author: Adam, @date: 7-31-2019 

Dynamic programming or recursion (slow). """

import time 

#%% Dynamic programming solution.

start_time = time.time()

n = 100
counts = [1] + [0] * n
for i in range(1, n):
    for j in range(i, n+1):
        counts[j] += counts[j - i]
print(counts[n])

print(time.time() - start_time)
                
                
#%% Recursive solution.

def count(n, m):
    if n == m:
        return 1 + count(n, m - 1)
    if (m == 0 or n < 0):
        return 0
    if (n == 0 or m == 1):
        return 1
    
    return count(n, m-1) + count(n-m, m)


start_time = time.time()

n = 10
print(count(n, n))

print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
                
                
                
                
                
                
                
                
                