""" @author: Adam, @date: 8-1-2019 

Dynamic programming, similar to p81 but optimizing columns at a time. """

import time 
import numpy as np

#%% Dynamic programming.

start_time = time.time()

# Extract data into 2D numpy array.
file = open("p81_matrix.txt")
text = file.read()
file.close()
rows = text.split("\n")[:-1]
rows = [row.split(",") for row in rows]
n = len(rows)
mat_data = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        mat_data[i, j] = int(rows[i][j])

# Copy data into matrix to contain minimum path sums at each point.
# Don't initialize cumulative sums in the last column because the path can
# terminate anywhere on the right!
mat_min_sums = np.copy(mat_data)
for col in range(n-2, -1, -1):
    
    min_candidates = np.zeros(n)
    
    # Assume going right or up is the best solution
    min_candidates[0] = mat_data[0, col] + mat_min_sums[0, col+1]
    for row in range(1, n):
        min_candidates[row] = (mat_data[row, col] 
                                + min(min_candidates[row-1], 
                                      mat_min_sums[row, col+1]))
                              
    
    # Given initial guesses, add down. Last row will be checked in next loop.
    min_candidates[0] = min(min_candidates[0], 
                            mat_data[0, col] + min_candidates[1])
    for row in range(1, n-1):
        min_candidates[row] = min(min_candidates[row],
                                  mat_data[row, col] + min_candidates[row+1],
                                  mat_data[row, col] + min_candidates[row-1])
    
    # Check all directions again, from the bottom up this time.
    min_candidates[n-1] = (mat_data[n-1, col] 
                            + min(min_candidates[n-2],
                                  mat_min_sums[n-1, col+1])
                          ) 
    for row in range(n-2, 0, -1):
        min_candidates[row] = (mat_data[row, col] 
                                + min(min_candidates[row+1], 
                                      min_candidates[row-1],
                                      mat_min_sums[row, col+1]
                                      )
                              )
    min_candidates[0] = (mat_data[0, col]
                          + min(min_candidates[1],
                                mat_min_sums[0, col+1])
                         )              
    
    mat_min_sums[:, col] = min_candidates
    
print(min(mat_min_sums[:, 0]))

print(time.time() - start_time)


#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
""" 

#%% Test data.
mat_data = np.array([[131, 673, 234, 103, 18],
                     [201, 96, 342, 965, 150],
                     [630, 803, 746, 422, 111],
                     [537, 699, 497, 121, 956],
                     [805, 732, 524, 37, 331]])
mat_min_sums = mat_data[:, :]
n = 5
                
                
                
                
                
                
                
                
                
                
                