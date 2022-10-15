""" @author: Adam, @date: 7-31-2019 

Use partition function generators. See
https://en.wikipedia.org/wiki/Partition_function_(number_theory)
for details. """

import time 

#%% Solution.

def P5(n):
    """Return generalized pentagonal number, n = 1, -1, 2, -2, 3, -3, ..."""
    return n*(3*n-1)//2


start_time = time.time()

# Keep track of p(n), n = 1, 2, 3, ...
p_dict = {0: 1}

# Keep track of growing list of pentagonal numbers
pent_counter = 1
pent_nums = [P5(pent_counter), P5(-pent_counter)]

# Initialize
n = 0
p = 1

# Compute p(1), p(2), ..., until p(n) mod 1,000,000 = 0.
while p % (int(1e6)) != 0:
    n += 1
    while pent_nums[-1] < n:  # Update pentagonal numbers if necessary.
        pent_counter += 1
        pent_nums.append(P5(pent_counter))
        pent_nums.append(P5(-pent_counter))
    
    # Loop through and sum all nonzero terms.     
    p = 0
    k = 1    
    even_counter = 0
    for num in pent_nums:
        x = n - num
        
        if x < 0:
            break
        
        if x in p_dict:
            p += (-1)**(k+1) * p_dict[x]
        else:  # Should not be empty!
            print(x, 'logic error')
        
        even_counter += 1
        if even_counter % 2 == 0:
            k += 1
    
    # Update dictionary.
    p_dict[n] = p
    
print(n)
print(p)

print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
                
                
                
                
                
                
                
                
                