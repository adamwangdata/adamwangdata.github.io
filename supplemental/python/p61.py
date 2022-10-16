""" @author: Adam, @date 7/22/2019 

Brute force solution. """
 
import time 

#%% Generate 4-digit polygonal numbers.

def P3(n):
    return n*(n+1) // 2

def P4(n):
    return n*n

def P5(n):
    return n*(3*n-1) // 2

def P6(n):
    return n*(2*n-1)

def P7(n):
    return n*(5*n-3) // 2

def P8(n):
    return n*(3*n-2)

def generate_polygonal(a, b, func):
    """Generate list of polygonal numbers in the range (a, b)."""
    nums = []
    i = 1
    while True:
        num = func(i)
        if num > a and num < b:
            nums.append(num)
        elif num > b:
            break
        i += 1
    return nums

def is_cyclic(a, b):
    """Test if the last two digits of a are the first two of b."""
    a_str = str(a)
    b_str = str(b)
    return a_str[-2:] == b_str[:2]


start = time.time() 

# Generate polygonal numbers between a and b.
a, b = 10**3, 10**4
functions = ['P3', 'P4', 'P5', 'P6', 'P7', 'P8']
num_dict = {}
for func in functions:
    num_dict[func] = generate_polygonal(a, b, eval(func))

print(time.time() - start)

#%% Find cyclical sets.

def search(seq, funcs, cyclical_sets):
    """Recursively find cyclical sets."""
    # Run only if one more polygonal list needs to be checked. Also check if 
    # the last and first digit are cyclic. If so, append to cyclical_sets.
    if len(funcs) == 1:  
        for n in num_dict[funcs[0]]:
            if is_cyclic(seq[-1], n) and is_cyclic(n, seq[0]):
                seq.append(n)
                cyclical_sets.append(seq)
   
    # Search exchaustively through all polygonal lists. If a potential match
    # is found, recursively continue the search.
    for func in funcs:
        for n in num_dict[func]:
            if is_cyclic(seq[-1], n):
                new_seq = seq + [n]
                new_funcs = [f for f in funcs if f != func]
                search(new_seq, new_funcs, cyclical_sets)

def has_repeat(nums):
    """Check if list of numbers has any repeat elements.""" 
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count > 1:
            return True
        
    return False


# Find all cyclical sets that match criterion 1.
start_func = 'P3'
remaining_funcs = [f for f in functions if f != start_func]
cyclical_sets = []
for n in num_dict[start_func]:
    seq = [n]
    search(seq, remaining_funcs, cyclical_sets)
    
# Filter out sets that do not match criterion 2.
for elem in cyclical_sets:
    if has_repeat(elem):
        cyclical_sets.remove(elem)
print(cyclical_sets, [sum(x) for x in cyclical_sets])
        
print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
"""

#%%
"""
# Nested loop solution. Comparable speed, but not readable.
start = time.time()
functions = ['P3', 'P4', 'P5', 'P6', 'P7', 'P8']
start_func = 'P3'
for n1 in num_dict[start_func]:
    funcs2 = [f for f in functions if f != start_func]
    for f2 in funcs2:
        for n2 in num_dict[f2]:
            if is_cyclic(n1, n2):
                funcs3 = [f for f in funcs2 if f != f2]
                for f3 in funcs3:
                    for n3 in num_dict[f3]:
                        if is_cyclic(n2, n3):
                            funcs4 = [f for f in funcs3 if f != f3]
                            for f4 in funcs4:
                                for n4 in num_dict[f4]:
                                    if is_cyclic(n3, n4):        
                                        funcs5 = [f for f in funcs4 if f != f4]
                                        for f5 in funcs5:
                                            for n5 in num_dict[f5]:
                                                if is_cyclic(n4, n5):        
                                                    funcs6 = [f for f in funcs5 if f != f5]
                                                    for f6 in funcs6:
                                                        for n6 in num_dict[f6]:
                                                            if is_cyclic(n5, n6) and is_cyclic(n6, n1):
                                                                print(n1, n2, n3, n4, n5, n6)
                                                                print(n1+n2+n3+n4+n5+n6)

print(time.time() - start)
"""
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
