""" @author: Adam, @date: 8-1-2019 

Dynamic programming, similar to p18 and p67, and Dijkstra's algorithm. """

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

# Copy data, and update minimum path sums later at each point. 
mat_min_sums = np.copy(mat_data)

# Work from bottom-right and update path sums based on only choice (vertical
# and horizontal edges) or min of two best possible choices.
for i in range(n-2, -1, -1):
    # Vertical and horizontal edge.
    mat_min_sums[n-1, i] += mat_min_sums[n-1, i+1]
    mat_min_sums[i, n-1] += mat_min_sums[i+1, n-1]
    
    # Remaining paths except diagonals.
    for j in range(n-2, i, -1):
        mat_min_sums[j, i] += min(mat_min_sums[j+1, i], mat_min_sums[j, i+1])
        mat_min_sums[i, j] += min(mat_min_sums[i, j+1], mat_min_sums[i+1, j])

    # Diagonals.
    mat_min_sums[i, i] += min(mat_min_sums[i, i+1], mat_min_sums[i+1, i])

print(mat_min_sums[0, 0])

print(time.time() - start_time)

#%% Dijkstra's algorithm. Slower than above, but more easily generalized.

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
        
# Mark unvisited modes nodes to never visit again by np.inf. Append minimum
# possible path sums to neighbors.  
node_marker = np.matrix(np.ones((n, n)) * np.inf)
i, j = 0, 0  # Initial node.
node_marker[i, j] = mat_data[i, j]
while True:
    
    # Check node below.
    if i < n-1:
        d_down = node_marker[i, j] + mat_data[i+1, j]
        node_marker[i+1, j] = min(node_marker[i+1, j], d_down)
    
    # Check node to the right.
    if j < n-1:     
        d_right = node_marker[i, j] + mat_data[i, j+1]
        node_marker[i, j+1] = min(node_marker[i, j+1], d_right)
    
    # Never visit again.
    node_marker[i, j] = np.inf
    
    if node_marker[n-1, n-1] < np.inf:  # we are done!
        break
    
    # Repeat search from node with smallest path sum.
    inds = np.where(node_marker == np.amin(node_marker))
    i = inds[0][0]
    j = inds[1][0]

print(node_marker[n-1, n-1])

print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
1)  It would be nice to visualize each algorithm
""" 

#%% Test data.
mat_data = np.array([[131, 673, 234, 103, 18],
                     [201, 96, 342, 965, 150],
                     [630, 803, 746, 422, 111],
                     [537, 699, 497, 121, 956],
                     [805, 732, 524, 37, 331]])
mat_min_sums = mat_data[:, :]
n = 5
                
                
                
                
                
                
                
                
                
                
                