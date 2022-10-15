""" @author: Adam, @date: 6-13-2019 """

import time
import numpy as np

def collatz_iter(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1

#%% Mostly brute force solution. Runs in ~42 s.
    
start = time.time()

test_range = 1000000
index_is_longest = np.ones(test_range + 1, dtype=bool)
index_is_longest[0] = False
len_max = 4
n_max = 1
for n in range(1, test_range + 1):

    if index_is_longest[n]:
        m = n  # copy starting point
        # Create Collatz sequence.
        seq = [n]
        while n > 1:
            n = collatz_iter(n)
            seq.append(n)
        len_seq = len(seq)
        subseq = [x for x in seq if x <= test_range]
        
        # Update previous max and boolean array testing longest sequence.
        if len_seq > len_max:
            index_is_longest[n_max] = False
            index_is_longest[subseq[1:]] = False
            len_max = len_seq
            n_max = m
        else: 
            index_is_longest[subseq] = False

print(n_max)
print(len_max)    

print(time.time() - start)


#%%
""" Potential improvements:
1)  Rather than only indicating if a value will lead to the longest chain, 
    store chain lengths so recalculation at non-starting values are reduced.
    Implement using a dictionary?
""" 
