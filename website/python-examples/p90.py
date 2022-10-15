""" @author: Adam, @date: 8-5-2019 

Brute force using itertools for combination generation."""

import time 
import itertools as it

#%% Solution.

# The following pairs must be spread across both dice. 
# 9 is treated as a 6. Combinations draw from 0 through 8, counting 6 twice.
pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), 
         (3, 6), (4, 6), (6, 4), (8, 1)]
def is_valid(comb1, comb2, pairs):
    """Check if dice containing faces comb1 and comb2 can enumerate all
    squares < 100. Pairs is a list of necessary pairings across dice."""
    for pair in pairs:
        n1 = pair[0]
        n2 = pair[1]
        if not((n1 in comb1 and n2 in comb2) or (n2 in comb1 and n1 in comb2)):
            return False
    return True


start_time = time.time()

count = 0
nums = [i for i in range(9)] + [6]
for comb1 in it.combinations(nums, 6):
    for comb2 in it.combinations(nums, 6):
        if is_valid(comb1, comb2, pairs):
            count += 1
print(count/2)  # Assume dice are indistinguishable, e.g. (d1, d2) = (d2, d1).

print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""