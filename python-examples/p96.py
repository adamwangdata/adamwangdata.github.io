""" @author: Adam, @date: 8-3-2019 

Brute-force backtracking algorithm."""

import time 
import numpy as np

#%% Data processing.

# Extract rows of text file.
file = open("p96_sudoku.txt")
text = file.read()
file.close()
rows = text.split("\n")

# Create list of puzzles, each represented as a list of strings.
puzzles = []
count = 1
puzzle = []
for row in rows[1:]:
    if count % 10 == 0:
        puzzles.append(puzzle)
        puzzle = []
    else:
        puzzle.append(row)
    count += 1
puzzles.append(puzzle)

# Convert each puzzle to a 9x9 numpy array.
grids = []
for puzzle in puzzles:
    for i in range(len(puzzle)):
        line = puzzle[i].strip()
        puzzle[i] = [int(char) for char in line]
    grids.append(np.array(puzzle))

#%% Backtracking solution.

def solve_sudoku(grid, print_sol=False):
    """Determine if Sudoku grid is solvable using backtracking, assuming a
    unique solution is defined. grid is updated in-place."""
    n_empty = 0  # Count empty entries as we search through the grid.
    
    # 4 loops to easily index each of 9 rows, columns, and 3x3 grids.
    # Start searching in top-left 3x3 grid.
    for row in range(3):
        for col in range(3):
            for subrow in range(3*row, 3*(row+1)):
                for subcol in range(3*col, 3*(col+1)):
                    
                    # Fill empty entries.
                    if grid[subrow, subcol] == 0:
                        n_empty += 1
                        
                        # For possible solutions satisfying Sudoku constraints,
                        # recursively continuing search with updated grid. 
                        # Backtrack if necessary.
                        for sol in range(1, 10):
                            if is_not_possible_sol(sol, grid,
                                                   row, col, subrow, subcol):
                                continue
                            else:  # sol may be a valid solution.
                                grid[subrow, subcol] = sol
                                if solve_sudoku(grid, print_sol):
                                    return True
                                else:  # No solution found; backtrack.
                                    grid[subrow, subcol] = 0
                        return False  # No possible solutions found; terminate 
                                      # this branch and backtrack.

    # If no empty entries counted (grid is complete), return True.
    is_solvable = (n_empty == 0)
    if is_solvable:
        if print_sol:
            print(grid)
    else:
        print("No solution found.")
    return is_solvable

def is_not_possible_sol(sol, grid, row, col, subrow, subcol):
    """Determine if sol may fill grid[subrow, subcol] given Sudoku 
    constraints."""
    return (   sol in grid[subrow, :]
            or sol in grid[:, subcol]
            or sol in grid[3*row:3*(row+1), 3*col:3*(col+1)]
            )
             
       
start_time = time.time()

# Solve all Sudoku puzzles and sum top-left 3 digit numbers.
s = 0
i = 0
for grid in grids:
    i += 1
    print('Grid', i)
    solve_sudoku(grid)
    
    n_str = ''
    for col in range(3):
        n_str = n_str + str(grid[0, col])
    s += int(n_str)

print(s)
    
print(time.time() - start_time)

#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
1)  Add visualizations to solving process.
"""
                
                
                
                
                
                