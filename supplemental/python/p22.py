""" @author: Adam, @date 6/16/2019 """

import time

def name_worth(name):
    """Return sum of alphabetical orderings for names in all uppercase."""
    worth = 0
    for char in name:
        worth += ord(char) - (ord("A") - 1)
    return worth
    
#%% Brute force.

if __name__ == '__main__':
    start = time.time()
    
    # Get contents of text file as a string.
    file = open("p22_names.txt")
    text = file.read()
    file.close()
    
    # Process into list of uppercase sorted names.
    text = text.replace('"', '').upper()
    names = text.split(",")
    names.sort()
    
    # Compute scores
    score = 0
    n = len(names)
    for i in range(n):
        score += name_worth(names[i]) * (i+1)
    print(score)
    
    print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
1)  This is slightly more difficult with proper capilizatized names like Adam 
    or Kathy. My line 22 and name_worth() convert and work with all uppercase.
"""
