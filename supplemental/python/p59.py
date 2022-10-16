""" @author: Adam, @date 7/17/2019 """

import time 
from p36 import to_base2

#%% Brute force.  

def xor(a, b):
    """Return a XOR b, where a and b are ASCII codes."""
    # Convert to binary and perform binary XOR.
    a_bin = str(to_base2(a))
    b_bin = str(to_base2(b))
    a_bin, b_bin = pad(a_bin, b_bin)
    out = ''
    for i in range(len(a_bin)):
        if a_bin[i] != b_bin[i]:
            out += '1'
        else:
            out += '0'
    
    # Convert back to base 10 ASCII.
    val = 0
    count = 0
    for char in out[::-1]:
        val += int(char) * 2**count
        count += 1
    return val

def pad(a, b):
    """Ensure numbers a and b are same length by front padding with zeros 
    if necessary."""
    a_len, b_len = len(a), len(b)
    if a_len == b_len:
        return a, b
    elif a_len > b_len:
        for i in range(a_len - b_len):
            b = '0' + b
        return a, b
    elif a_len < b_len:
        for i in range(b_len - a_len):
            a = '0' + a
        return a, b
    
    
start = time.time()

# Get contents of text file as a string.
file = open("p59_cipher.txt")
text = file.read()
file.close()

# Split into ASCII codes, try all possible passwords, and print message/key
# if contains the decrpyted message contains " the " and  " of " with 
# leading/trailing spaces.
codes = text.split(',')
for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        for k in range(ord('a'), ord('z') + 1):
            message = ''
            key = [i, j, k]
            count = 0
            for code in codes:
                #message += chr(xor(key[count % 3], int(code)))  # Works, but slow.
                message += chr(key[count % 3] ^ int(code))
                count += 1
            if ' the ' in message and ' of ' in message:
                print(message, key)
                ans = 0
                for char in message:
                    ans += ord(char)
                print(ans)

print(time.time() - start)


#%%
""" Potential Improvements:
1)  Natural language processing, e.g. letter frequency analysis to determine
    likely key values. 

    Extensions / Remarks:
1)  Password is [101, 120, 112] corresponding to 'exp'.
"""  























