# ---
# jupyter:
#     jupytext:
#         text_representation:
#             extension: .py
#             format_name: percent
#     kernelspec:
#         language: python
#         name: python3
#         display_name: Python 3.7.6
# ---




#%% [markdown] Macros Setup tags=['remove-cell']
# $$
# \newcommand{\parens}[1]{\mathopen{}\left(#1\right)\mathclose{}}
# \newcommand{\bracks}[1]{\mathopen{}\left[#1\right]\mathclose{}}
# \newcommand{\braces}[1]{\mathopen{}\left\{#1\right\}\mathclose{}}
# \newcommand{\abs}[1]{\mathopen{}\left\lvert#1\right\rvert\mathclose{}}
# \newcommand{\norm}[1]{\mathopen{}\left\lVert#1\right\rVert\mathclose{}}
# \renewcommand{\vec}[1]{\boldsymbol{\mathbf{#1}}}
# \newcommand{\mat}[1]{\mathbf{#1}}
# \newcommand{\tpose}[1]{#1^T}
# \newcommand{\inv}[1]{#1^{-1}}
# \newcommand{\Matrix}[1]{
#   \begin{bmatrix}
#     #1
#   \end{bmatrix}
# }
# \newcommand{\seq}[1]{1, 2, \ldots, #1}
# \newcommand{\reals}{\mathbb{R}}
# \newcommand{\mper}{\,\text{.}}
# \newcommand{\mcom}{\,\text{,}}
# $$

#%% [markdown]

"""
# Project Euler

[Project Euler](https://projecteuler.net/about) is a series of computational problems that, generally speaking, can be solved by a computer in less than a minute.
At least, that was my goal when solving them.

```{margin}
The magic 100 number may also have been motivated by [Wes McKinney's blog post](https://wesmckinney.com/blog/im-moving-to-san-francisco-and-hiring/) where he gives "Extra points if you have [solved 100 or more problems on Project Euler]".
```
Occasionally the simplest brute force algorithm works, but often clever modifications are required.
In many cases, advanced mathematics (e.g. number theory) is required, which is why I stopped after 100 problems.
You can find my all 100 of my solutions [here](https://github.com/adamwangdata/adamwangdata.github.io/tree/main/python-examples), but I wanted to highlight a few particularly interesting ones.

## Problem 96: Sudoku

[Problem 96](https://projecteuler.net/problem=96) is one of my favorites.
The goal is to solve a [Sudoku](https://en.wikipedia.org/wiki/Sudoku) puzzle algorithmically.
The crude brute force method is obviously too slow, but the space of possible valid solutions can be drastically reduced by applying the constraints of the game: each digit 1 to 9 must be present in each row, column, and 3 by 3 subgrid.
I settled on an algorithm that systematically fills one digit at a time with a candidate solution, i.e. one that satisfies the Sudoku constraints.
It keeps on filling digits until either the grid is complete, meaning the puzzle has been solved, or no candidate solutions exist.
In the latter case, the algorithm must backtrack to a previous state that could have more candidate solutions, and continue its search.
I implemented this guess and backtrack via recursion.

```{margin}
The current puzzle was designed to be difficult (for humans, at least) by mathematician Arto Inkala, taken from [this article](https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html).
```
Given a 3 by 3 `numpy` array representing a Sudoku grid, the following `solve_sudoku()` function prints the solution if it is solvable.
```{note}
You can try out the code without leaving this page!
Hover over the {fa}`rocket` launch button at the top of this page, then click the {guilabel}`Live Code` button.
You can even modify the code so if you're having trouble with a Sudoku puzzle, just modify `puzzle` to your liking. Zeros are interpreted as empty cells.
```
"""

#%%

import numpy as np

def solve_sudoku(grid, print_sol=False):
    """Solve a Sudoku grid using backtracking, assuming a
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
    """Determine if sol may fill element grid[subrow, subcol] given Sudoku
    constraints."""
    return (   sol in grid[subrow, :]
            or sol in grid[:, subcol]
            or sol in grid[3*row:3*(row+1), 3*col:3*(col+1)]
            )

# Initialize a puzzle. Zeros represent empty cells.
puzzle = """800000000
            003600000
            070090200
            050007000
            000045700
            000100030
            001000068
            008500010
            090000400"""

# Convert string puzzle to 9x9 numpy array of integers.
puzzle = puzzle.split("\n")
for i in range(len(puzzle)):
    line = puzzle[i].strip()
    puzzle[i] = [int(char) for char in line]
grid = np.array(puzzle)
print("initial grid:")
print(grid)

# Solve the puzzle!
print("solving...")
solve_sudoku(grid, print_sol=True);

#%% [markdown]

"""
## Another problem

## And one more
"""