""" @author: Adam, @date: 8-7-2019 

Brute force, just under 1 minute."""

import time 

#%% Solution.

squares_dict = {}
for i in range(10):
    squares_dict[i] = i**2
    
def sum_digit_squares(n, squares_dict):
    """Return some of squares of digits of n."""
    s = 0
    for char in str(n):
        s += squares_dict[int(char)]
    return s


start_time = time.time()

# Memoize chains leading to 1 or 89.
chains1 = {1}
chains89 = {89}

limit = int(1e7)
count = 0
for n in range(1, limit):
    chain = set()
    while True:
        if n in chains1:
            chains1 = chains1 | chain
            break
        if n in chains89:
            count += 1
            chains89 = chains89 | chain
            break
        n = sum_digit_squares(n, squares_dict)
        chain.add(n)
print(count)
    

print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
1)  Use number combinations to reduce the search space. e.g., 1234567 yields 
    same result as 2134567 since their sum of digit squares is the same.
2)  Note that the maximum element in a chain after iteration is 7*(9^7).
    
    Extensions/Remarks:
"""