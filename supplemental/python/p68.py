""" @author: Adam, @date 7/25/2019 

Brute force. 
"""

import time 
import itertools as it

#%% Find maximum 16-digit string for "magic" n-gon rings.

def get_base_node_pairs(a, b):
    """For a magic (b-a)/2-gon ring filled with integers in [a, b),
    return list of base and node pairs with equal totals along all lines."""
    n = (b - a) // 2
    base_node_pairs = []
    
    # Try all possible permutations of base-node number combinations.
    # Ensure resultant base_node_pairs have equal totals along all lines
    # and are unique.
    for perm in it.permutations(range(a, b), b-a):
        totals = []
        base = [perm[i] for i in range(0, n)]
        nodes = [perm[i] for i in range(n, b-1)]
        if nodes[0] == min(nodes):  # Avoid rotations of the n-gon.
            for i in range(n):
                total = base[i % n] + base[(i+1) % n] + nodes[i]
                totals.append(total)
                if total != totals[0]:  # Totals must be same.
                    break
            else:
                base_node_pairs.append((base, nodes))
    return base_node_pairs

def base_node_pairs_to_sets(base_node_pairs, n):
    """Given a base_node_pair, return the stringed solution."""
    sols = []
    for elem in base_node_pairs:
        base, nodes = elem[0], elem[1]
        if nodes[0] == min(nodes):
            sol = ''
            for i in range(n):
                sol += str(nodes[i]) + str(base[i % n]) + str(base[(i+1) % n])
            sols.append(sol)
    return(sols)

def m_digit_sols(sols, m):
    """Filter solutions to those with m digits."""
    m = 16
    m_sols = []
    for sol in sols:
        if len(sol) == m:
            m_sols.append(sol)
    return m_sols


start_time = time.time()

a, b = 1, 11  # Range of numbers used
n = (b - a) // 2
m = 16
base_node_pairs =  get_base_node_pairs(a, b)
sols = base_node_pairs_to_sets(base_node_pairs, n)
m_sols = m_digit_sols(sols, m)
m_sols = [int(char) for char in m_sols]
print(max(m_sols))

print(time.time() - start_time)

#%% Further comments.
""" Potential Improvements:
1)  Reduce number of permutations checked, e.g. 10 cannot be in the base for
    a 16-digit string since 10 will be summed twice. 
    
    Extensions / Remarks:
"""
