""" @author: Adam, @date: 8-1-2019 

Dijkstra's algorithm. """

import time 
import numpy as np

#%% Dijkstra's algorithm.

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

    # Check node above.    
    if i > 0:
        d_up = node_marker[i, j] + mat_data[i-1, j]
        node_marker[i-1, j] = min(node_marker[i-1, j], d_up)

    # Check node to the right.
    if j < n-1:     
        d_right = node_marker[i, j] + mat_data[i, j+1]
        node_marker[i, j+1] = min(node_marker[i, j+1], d_right)
 
    # Check node to the left.
    if j > 0:
        d_left = node_marker[i, j] + mat_data[i, j-1]
        node_marker[i, j-1] = min(node_marker[i, j-1], d_left)
        
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
""" 

#%% Test data.
mat_data = np.array([[131, 673, 234, 103, 18],
                     [201, 96, 342, 965, 150],
                     [630, 803, 746, 422, 111],
                     [537, 699, 497, 121, 956],
                     [805, 732, 524, 37, 331]])
mat_min_sums = mat_data[:, :]
n = 5
                
                
                
                
                
                
                
                
                
                
                