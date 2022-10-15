""" @author: Adam, @date 6/20/2019

The problem is to sum to a value val using coins. This can be solved 
recursively by noting that once we use the largest coin, then 
    val' = val - (largest coin),
and the problem is to solve for val' using coins and also counting the
ways to use all coins but the largest coin.
"""

import time

#%% Recursion.

def count_ways(val, coin_index, coins):
    ways = 0
    if val < 0:
        return 0
    elif val == 0 or coin_index == 0:
        return 1
    else:
        while val >= 0:
            ways += count_ways(val, coin_index-1, coins)
            val -= coins[coin_index]
        return ways

start = time.time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]  # England 
#coins = [1, 5, 10, 25]  # US
val = 200
print(count_ways(val, len(coins)-1, coins))

print(time.time() - start)

#%% Brute force, bad code.

start = time.time()

# Loop through all possible configurations of coins c2 to c8
c1, c2, c3, c4, c5, c6, c7, c8 = 1, 2, 5, 10, 20, 50, 100, 200
val = 200
totals = []
for i8 in range(0, val//c8 + 1):
    for i7 in range(0, val//c7 + 1):
        for i6 in range(0, val//c6 + 1):
            for i5 in range(0, val//c5 + 1):
                for i4 in range(0, val//c4 + 1):
                    for i3 in range(0, val//c3 + 1):
                        for i2 in range(0, val//c2 + 1):
                            totals.append((i8*c8 + i7*c7 + i6*c6 + i5*c5
                                            + i4*c4 + i3*c3 + i2*c2))
for coin in coins:
    for i in range(0, val//coin + 1):
        totals.append()
# It 0 <= total <= val, some amount of c1 can achieve value.
ways = 0
for total in totals:
    if total >= 0 and total <= val:
        ways += 1
print(ways)
        
print(time.time() - start)

#%%
""" Potential Improvements:
    
    Extensions / Remarks:
1)  Remove the coin with value 1.
"""