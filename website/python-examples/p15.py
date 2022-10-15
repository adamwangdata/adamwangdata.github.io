""" @author: Adam, @date: 6-14-2019 

This problem has an easy combinatorics solution. For a (n by m) grid, you must
take a total of (n + m) steps; n of those must be right and m must be down.
Thus, how many ways can we choose n right steps out of a total of (n + m)?
The answer is the binomial coefficient ((n+m) choose n).

For a  programmatic approach, we can also use recursion. Starting from (0, 0), 
the number of paths to reach (n, m) is equal to the number of paths to reach 
(n - 1, m) plus the number of paths to reach (n, m - 1); this is because once 
at (n - 1, m) or (n, m - 1), there is only one path to (n, m). I implement 
this here with memoization for a sizable speed boost.
"""

import time

def count_paths(n, m):
    """Count the number of paths consisting of right and down steps in an 
    (n by m) grid."""
    if n == 0:
        return 1
    elif m == 0:
        return 1
    else:
        return count_paths(n - 1, m) + count_paths(n, m - 1)

def count_paths_memoized(n, m):
    """Memoized version of count_paths(). Requires initialization of 
    path_counts dictionary storing counts for (a by b) grids, a<=n, b<=m."""
    if n == 0:
        return 1
    elif m == 0:
        return 1
    elif (n, m) in path_counts:
        return path_counts[(n, m)]
    else:
        path_counts[(n, m)] = (count_paths_memoized(n - 1, m)
                               + count_paths_memoized(n, m - 1))
    return path_counts[(n, m)]

#%% Recursion with memoization.
    
start = time.time()

n, m = 20, 20
path_counts = {}
#print(count_paths(n, m))  # Slow.
print(count_paths_memoized(n, m))

print(time.time() - start)


