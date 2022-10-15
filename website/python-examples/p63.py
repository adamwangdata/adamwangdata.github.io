""" @author: Adam, @date 7/24/2019

Only need to consider i**n, i = 1, 2, ..., 9. For i >= 10, i**n will always
have more digits than n. Furthermore, n <= 21 since len(str(9**22)) = 21, i.e.
i**n will always have fewer digits than n."""

import time 

#%% Hard-coded bounds count. 
    
start = time.time()

count = 0
for n in range(1, 22):
    for i in range(1, 10):
        num = i**n
        num_digits = len(str(num))
        if num_digits == n:
            count += 1        
        
print(time.time() - start)  

#%% No upper-bound.  
    
start = time.time()

count = 0
for n in range(1, 1000):
    i = 1
    num = i**n
    num_digits = len(str(num))
    while num_digits <= n:
        if num_digits == n:
            count += 1
        i += 1
        num = i**n
        num_digits = len(str(num))

print(time.time() - start)   
 
#%% Further comments.
""" Potential Improvements:
    
    Extensions / Remarks:
1)  See below for (perhaps) more straightforward algorithms that run
    into precision / big number problems.
"""