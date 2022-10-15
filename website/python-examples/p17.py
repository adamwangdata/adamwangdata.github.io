""" @author: Adam, @date: 6-14-2019 """

import time

# Dictionary mapping numerical values to strings.
single = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
          8:'eight', 9:'nine'}
teen = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
tens = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 
        6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

def int2d_to_words(n):
    """Return string representation of 1- to 2-digit integers."""
    if n < 10:  # Single digits.
        return single[n]
    elif n > 10 and n < 20:  # Teens.
        return teen[n]
    else:  # Double digits except teens.
        rem = n % 10
        if rem == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + ' ' + single[rem]

def int3d_to_words(n):
    """Return string representation of 3-digit integers."""
    rem = n % 100
    if rem == 0:
        return single[n // 100] + ' hundred'
    else:
        return single[n // 100] + ' hundred and ' + int2d_to_words(rem)

def int_to_words(n):
    """Return string representation of 1- to 3-digit integers."""
    if n < 100:
        return int2d_to_words(n)
    else:
        return int3d_to_words(n)
        

#%% Count.
    
start = time.time()

n = 1000
count = 0
for i in range(1, n):
    count += len(int_to_words(i).replace(' ', ''))
count += len("one thousand".replace(' ', ''))
print(count)

print(time.time() - start)


#%%
""" Potential improvements:
1)  Only store length rather than full strings and don't include spaces. 
    But I prefer this "uncompressed" solution for use and ease of testing.
""" 
