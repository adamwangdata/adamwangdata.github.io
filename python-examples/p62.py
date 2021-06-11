""" @author: Adam, @date 7/22/2019 

Brute force solution. """
 
import time 

#%% Find smallest cube with target permutations.

from p49 import are_permutations

def check_cube_perms(cubes, target):
    """For a list of cubes, check if that list has a subset with target
    number of permutations. Return the smallest permutation in the set."""
    n = len(cubes)
    for i in range(n):
        a = cubes[i]
        count = 0
        for j in range(i, n):
            b = cubes[j]
            if are_permutations(a, b):
                count += 1
        if count == target:
            return a
    
    return None


start = time.time()

# Generate list of cubes in the range [10^a, 10^(a+1)), a = 0, 1, 2, ...
# For each set of n-digit cubes, check if a set of target permutations exists.
target = 5
cubes = []
i = 1
upper_bound = 10
while True:
    cube = i**3
    
    if cube > upper_bound:
        res = check_cube_perms(cubes, target)
        if res != None:
            print(res)
            break
        upper_bound *= 10
        cubes = []
        
    cubes.append(cube)
    i += 1
    
print(time.time() - start)
#%% Further comments.
""" Potential Improvements:
1)  Reduce the sample space of permutation checking by representing each
    number as a sum of digits. Then only check those with the same digit sum.
2)  Sort all numbers. If the sorted representations are equal, they are 
    permutations.    
    
    Extensions / Remarks:
"""

            
            
            
            
