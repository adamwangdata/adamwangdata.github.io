""" @author: Adam, @date 6/25/2019 """

from p22 import name_worth as get_word_val
import time

def get_triangle_numbers(n):
    """Return set of the triangle numbers <= n."""
    nums = set()
    i = 1
    while True:
        num = i*(i+1)//2
        if num > n:
            break
        nums.add(num)
        i += 1
        
    return nums

#%% Brute force.

start = time.time()

# Get contents of text file as a string.
file = open("p42_words.txt")
text = file.read()
file.close()

# Process into list of uppercase words.
text = text.replace('"', '').upper()
words = text.split(",")

# Compute word values and triangle numbers up to max value.
word_vals = []
for word in words:
    word_vals.append(get_word_val(word))
max_val = max(word_vals)
tri_nums = get_triangle_numbers(max_val)

# Count number of triangle words.
count = 0
for val in word_vals:
    if val in tri_nums:
        count += 1
print(count)

print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
"""
