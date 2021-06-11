""" @author: Adam, @date: 8-9-2019 

Brute force. """

import time 
import itertools as it

#%% Extract list of words
file = open("p98_words.txt")
text = file.read()
file.close()
words_with_quotes = text.split(",")
words = []
for word in words_with_quotes:
    word = word.strip('"')
    words.append(word)

#%% Brute force solution, given list of words.

def are_anagrams(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


start_time = time.time()

# All squares up to 10**9 (10 digit number) 
squareset = {i**2 for i in range(1, int(10**(10/2)))}

max_square = 0
max_square_pairs = []
n_words = len(words)
# Loop through all word pairs.
for i in range(n_words):
    word1 = words[i]
    for j in range(i+1, n_words):
        word2 = words[j]
        
        # For anagrams, determine which digitial substitutions form squares.
        # Record largest square found and associated words. 
        if are_anagrams(word1, word2):
            word_len = len(word1)
            unique_letters = list(dict.fromkeys(word1))
            n_digits = len(unique_letters)
            
            # Pre-generate list of possible squares, rather than searching
            # through all possible permutations of digital substitutions.
            squares = [i**2 for i in range(int(10**((n_digits-1)/2))+1, 
                                           int(10**(n_digits/2)))]
            for square in squares:
                square = list(str(square))
                if len(set(square)) != n_digits:
                    continue
                
                # Dictionary mapping letters to digits.
                d = {}
                for k in range(n_digits):
                    d[unique_letters[k]] = square[k]
                
                # Convert words to numbers
                n1_str = ''
                n2_str = ''
                for k in range(word_len):
                    n1_str = n1_str + str(d[word1[k]])
                    n2_str = n2_str + str(d[word2[k]])
                
                # Check if both words are squares with no leading zeros.
                n1 = int(n1_str)
                n2 = int(n2_str)    
                if n1 in squareset and n2 in squareset:
                    if len(str(n1)) == len(str(n2)):
                        square = max(n1, n2)
                        if square > max_square:
                            max_square = square
                            max_square_pairs = [word1, word2]
print(max_square, max_square_pairs)

print(time.time() - start_time)


#%% Bruter force, trying all possible permutations of digital substitusions.

def are_anagrams(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))

start_time = time.time()


# All squares up to 10**9 (10 digit number) 
squareset = {i**2 for i in range(1, int(10**(10/2)))}
count = 0
max_square = 0
n_words = len(words)
for i in range(n_words):
    print(i, count, max_square)
    word1 = words[i]
    for j in range(i+1, n_words):
        word2 = words[j]
        
        if are_anagrams(word1, word2):
            count += 1
            word_len = len(word1)
            unique_letters = list(set(word1))
            n_digits = len(unique_letters)
            for perm in it.permutations(range(10), n_digits):
                d = {}
                for k in range(n_digits):
                    d[unique_letters[k]] = perm[k]
                
                n1_str = ''
                n2_str = ''
                for k in range(word_len):
                    n1_str = n1_str + str(d[word1[k]])
                    n2_str = n2_str + str(d[word2[k]])
                
                n1 = int(n1_str)
                n2 = int(n2_str)
                if n1 in squareset and n2 in squareset:
                    if len(str(n1)) == len(str(n2)):
                        print(word1, word2)
                        square = max(n1, n2)
                        if square > max_square:
                            max_square = square
print(max_square)
            

print(time.time() - start_time)


                
#%% Comments.
""" Potential improvements:
1)  Pre-generate lists of squares with 1, 2, ..., n digits.
    
    Extensions/Remarks:
"""




