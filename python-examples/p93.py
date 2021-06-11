""" @author: Adam, @date: 8-7-2019 

Brute force all possible operations for each of the 5 expressions with 
parentheses, @ being any operator. Evaluation order without parenthesis is 
left to right.

a @ b @ c @ d
a @ (b @ c) @ d
a @ ((b @ c) @ d)
a @ (b @ (c @ d))
(a @ b) @ (c @ d)
"""

import time 
import itertools as it

#%% Solution.

def count_streak(nums):
    """Count number of conscecutive integers 1 to n, assuming min(nums) = 1."""
    nums = list(nums)
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] != (i + 1):
            return i
    return n
    

start_time = time.time()

n_digits = 4
operations = ['+', '-', '*', '/']

max_count = 0
max_digits = []
max_results = set()
# Loop through all digit sets.
for digit_tup in it.combinations(range(0, 10), n_digits):
    results = set()  # Store results of all arithemtic expressions.
    
    # Loop through all possible digit orderings with all possible operations
    for digits in it.permutations(digit_tup, n_digits): 
        for ops_tup in it.product(operations, repeat=3):

            # Base expression with no parenthesis.            
            base = str(digits[0])
            for i in range(n_digits-1):
                base = base + ops_tup[i] + str(digits[i+1])
                
            # Five parenthesis configurations, using eval().
            try:
                res1 = eval(base)
            except ZeroDivisionError:
                res1 = 0
            try:
                res2 = eval(base[:2] + '(' + base[2:5] + ')' + base[5:])
            except ZeroDivisionError:
                res2 = 0
            try:
                res3 = eval(base[:2] + '((' + base[2:5] + ')' + base[5:] + ')')
            except ZeroDivisionError:
                res3 = 0
            try:
                res4 = eval(base[:2] + '(' + base[2:4] + '(' + base[4:] + '))')
            except ZeroDivisionError:
                res4 = 0
            try:
                res5 = eval('(' + base[:3] + ')' + base[3] + '(' + base[4:] + ')')
            except ZeroDivisionError:
                res5 = 0
            
            # Append unique results.
            for i in range(1, 6):
                res_str = 'res' + str(i)
                res = eval(res_str)
                if res > 0 and int(res) == res:
                    results.add(res)         
    
    # Track maximum streak and associated digits
    count = count_streak(results)
    if count > max_count:
        max_count = count
        max_digits = digits
        max_results = results
    
print(max_digits, max_count)
print(max_results)
    
print(time.time() - start_time)
                
#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""








