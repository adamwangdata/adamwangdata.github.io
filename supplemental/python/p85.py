""" @author: Adam, @date: 8-4-2019 

Brute force. """

import time 

#%% Brute force solution.

def count_rects(h, w):
    """Count number of subrectangles in rectangle of dimensions h x w."""
    count = 0
    
    # Count rectangles of all possible subheights 1, 2, ..., h.
    for sub_h in range(1, h+1):
        sub_count = 0
        
        # For each subheight, count number of rectangles of each subwidth
        # 1, 2, ..., w. 
        for sub_w in range(1, w+1):
            #sub_count += (w - sub_w) + 1  # More intuitive, but slower.
            sub_count += sub_w  # Same result as above line due to symmetry.
        sub_count *= (h - sub_h) + 1  # Count vertical translations.
        
        count += sub_count
        
    return count
        

start_time = time.time()

n = int(2e6)         # Target rectangle count
min_dist = int(2e6)  # Distance to minimize
min_dist_count = 1   # Associated count
area = int(2e6)      # Associated area.

# Deduce maximum dimension based on width 1 rectangle.
h = 1
while count_rects(h, 1) < n:
    h += 1
limit = h

# Loop through all possible candidate rectangles, updating the area of the
# nearest rectangle.
for h in range(limit):
    i = 0  # Keep track of iterations in below loop.
    for w in range(h, limit):
        print(min_dist_count)
        count = count_rects(h, w)
        dist = abs(count - n)
        if dist < min_dist:  # Update area and associated variables.
            min_dist = dist
            min_dist_count = count
            area = h*w
            
        if count > min_dist_count + 2*min_dist:  # Count will only get larger, 
            break                                # so break.
        
        i += 1
        
    if i == 0:  # Counts will only get larger, so break.
        break
        
print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 
                
                
"""
1xn: 1 3 6 10 ... 
2xn: 1 3 6 10 ..."""                
                
                
                
                
                
                
                