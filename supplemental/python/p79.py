""" @author: Adam, @date: 7-31-2019 

Solvable by hand. There are no repeat digits in each code and 8 unique digits
across all codes. Thus the minimum number is an 8 digit number. Orderings
must then obey each code. 7 is always in front and 0 is always last. Dropping
those, 3 is always in front and 9 is always last. Proceeding, deduce the 
password is 73162890. Brute force implementation below."""

import time 

#%% Brute force solution.

def is_possible_sol(n, code):
    """Check if n is a possible password given 3-digit code."""
    n_str = str(n)
    code_str = str(code)
    
    for char in code_str:
        try:
            i = n_str.index(char)
            n_str = n_str[i+1:]
        except ValueError:
            return False

    return True


start_time = time.time()

# Process into list of unique successful codes.
file = open("p79_keylog.txt")
text = file.read()
file.close()
codes = text.split("\n")[:-1]
unique_codes = []
for code in codes:
    if code not in unique_codes:
        unique_codes.append(code)

# Extract number of unique digits for starting guess.
digits = []
for code in unique_codes:
    for char in str(code):
        digits.append(int(char))
n_digits = len(set(digits))

sol = 10**(n_digits-1)
while True:
    sol_str = str(sol)
    if '4' in sol_str or '5' in sol_str:
        sol += 1
        continue
    
    for code in unique_codes:
        if is_possible_sol(sol, code) == False:
            break
    else:
        break
    sol += 1

print(sol)

print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
                
                
                
                
                
                
                
                
                