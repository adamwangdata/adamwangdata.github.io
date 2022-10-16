""" @author: Adam, @date: 8-6-2019 

Convert to numeric values, then back to minimal Roman numerals. """

import time 

#%% Solution.

roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman_to_n(roman):
    """Convert a Roman numeral to its numeric value."""
    s = 0
    str_len = len(roman)
    i = 0
    while i < str_len:
        if i == (str_len - 1):  # Don't check for subtractive pairs
            s += roman_dict[roman[i]]
            break
        
        # Add value, accounting for subtracive pairs.
        val = roman_dict[roman[i]]
        next_val = roman_dict[roman[i+1]]
        if val < next_val:
            s += next_val - val
            i += 2
        else:
            s += val
            i += 1
    return s

# Possible values and Roman numeral combinations to add.
roman_options = [(900, 'CM'), (500, 'D'), (400, 'CD'), 
                 (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]        

def n_to_roman(n, options):
    """Convert a number to its minimal Roman numeral representation."""
    
    # Pad with largest denomination M
    roman = '' + 'M' * (n // 1000)
    n = n % 1000
    
    # Iteratively append to Roman numeral, depending on option.
    for option in roman_options:
        val = option[0]
        letters = option[1]
        while n >= val:
            n -= val
            roman += letters
    
    return roman


# Extract list of valid Roman numerals.
file = open("p89_roman.txt")
text = file.read()
file.close()
romans = text.split("\n")

# Sum difference between original and minimal representation.
start_time = time.time()

count = 0
for roman in romans:
    n_original = len(roman)
    n_minimal = len(n_to_roman(roman_to_n(roman), roman_options))
    count += (n_original - n_minimal)
print(count)

print(time.time() - start_time)

#%% Comments.
""" Potential improvements:
    
    Extensions/Remarks:
"""


                
                