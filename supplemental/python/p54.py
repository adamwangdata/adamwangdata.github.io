""" @author: Adam, @date 7/17/2019 """

import time

#%% Brute force. Write functions to determine hand rank, treating ties.

def read_hands(hands):
    """Read each line of p42_poker.txt as two hands, each a list of tuples
    containing the integer card value and its suit."""
    h1, h2 = [], []
    for i in range(5):
        card = hands[i]
        h1.append((int_card_val(card[0]), card[1]))
    for i in range(5, 10):
        card = hands[i]
        h2.append((int_card_val(card[0]), card[1]))
    return h1, h2

def int_card_val(val):
    """Return integer value of a card."""
    if val == 'T':
        return 10
    elif val == 'J':
        return 11
    elif val == 'Q':
        return 12
    elif val == 'K':
        return 13
    elif val == 'A':
        return 14
    else:
        return int(val)
    
def split_val_suit(hand):
    """Split output of read_hands() into two lists of values and suits."""
    vals = []
    suits = []
    for card in hand:
        vals.append(card[0])
        suits.append(card[1])
    return vals, suits
    
def is_straight_or_flush(vals, suits, flush=True, straight=False, royal=False):
    """Check if a hand is a straight, flush, straight flush, or royal flush.
    By default checks flush only."""
    # Check if all suits are the same.
    if flush:
        if len(set(suits)) > 1:
            return False
        
    # Check if all values are conscecutive.
    if straight:
        vals.sort()
        if royal:
            base = 10
        else:
            base = min(vals)
        for val in vals:
            if val == base:
                base += 1
                continue
            else:
                return False
            
    return True
    
def is_n_of_a_kind(vals, n):
    """Check if hand has n of a kind."""
    unique_vals = set(vals)
    for unique_val in unique_vals:
        count = 0
        for val in vals:
            if unique_val == val:
                count += 1
        if count == n:
            return True
    return False

def is_full_house(vals):
    """Check if hand is full house."""
    return is_n_of_a_kind(vals, 3) and is_n_of_a_kind(vals, 2) 

def is_two_pair(vals):
    """Check if hand has two pairs."""
    n_pairs = 0    
    unique_vals = set(vals)
    for unique_val in unique_vals:
        count = 0
        for val in vals:
            if unique_val == val:
                count += 1
        if count == 2:
            n_pairs += 1
    return n_pairs == 2

def play(h1, h2, wins1, wins2, print_tests=False):
    """Increment win count for the player that wins. Sequentially try
    lower ranks, starting from a royal flush. In the case of a tie, neither
    win count is incremented."""
    v1, s1 = split_val_suit(h1)
    v2, s2 = split_val_suit(h2)
    
    # Test royal flush.
    if print_tests == True: print("Testing royal flush.")
    h1_rf = is_straight_or_flush(v1, s1, flush=True, straight=True, royal=True)
    h2_rf = is_straight_or_flush(v2, s2, flush=True, straight=True, royal=True)
    if h1_rf and not h2_rf:
        wins1 += 1
        return wins1, wins2 
    elif not h1_rf and h2_rf:
        wins2 += 1
        return wins1, wins2     
    elif h1_rf and h2_rf:
        return wins1, wins2
    
    # Test straight flush.
    if print_tests == True: print("Testing straight flush.")
    h1_sf = is_straight_or_flush(v1, s1, 
                                 flush=True, straight=True, royal=False)
    h2_sf = is_straight_or_flush(v2, s2, 
                                 flush=True, straight=True, royal=False)
    if h1_sf and not h2_sf:
        wins1 += 1
        return wins1, wins2 
    elif not h1_sf and h2_sf:
        wins2 += 1
        return wins1, wins2     
    elif h1_sf and h2_sf:
        return play_highcard(v1, v2, wins1, wins2)
    
    # Test four of a kind
    if print_tests == True: print("Testing four of a kind.")
    h1_4k = is_n_of_a_kind(v1, 4)
    h2_4k = is_n_of_a_kind(v2, 4)
    if h1_4k and not h2_4k:
        wins1 += 1
        return wins1, wins2 
    elif not h1_4k and h2_4k:
        wins2 += 1
        return wins1, wins2     
    elif h1_4k and h2_4k:
        return play_nkind_tiebreak(v1, v2, wins1, wins2, 4)
                
    # Test full house
    if print_tests == True: print("Testing full house.")
    h1_fh = is_full_house(v1)
    h2_fh = is_full_house(v2)
    if h1_fh and not h2_fh:
        wins1 += 1
        return wins1, wins2 
    elif not h1_fh and h2_fh:
        wins2 += 1
        return wins1, wins2     
    elif h1_fh and h2_fh:
        # Note: cannot tie when comparing 3 of a kinds.
        return play_nkind_tiebreak(v1, v2, wins1, wins2, 3)
        
    # Test flush.
    if print_tests == True: print("Testing flush.")
    h1_f = is_straight_or_flush(v1, s1, 
                                 flush=True, straight=False, royal=False)
    h2_f = is_straight_or_flush(v2, s2, 
                                 flush=True, straight=False, royal=False)
    if h1_f and not h2_f:
        wins1 += 1
        return wins1, wins2 
    elif not h1_f and h2_f:
        wins2 += 1
        return wins1, wins2     
    elif h1_f and h2_f:
        return play_highcard(v1, v2, wins1, wins2)
    
    # Test straight.
    if print_tests == True: print("Testing straight.")
    h1_s = is_straight_or_flush(v1, s1, 
                                 flush=False, straight=True, royal=False)
    h2_s = is_straight_or_flush(v2, s2, 
                                 flush=False, straight=True, royal=False)
    if h1_s and not h2_s:
        wins1 += 1
        return wins1, wins2 
    elif not h1_s and h2_s:
        wins2 += 1
        return wins1, wins2     
    elif h1_s and h2_s:
        return play_highcard(v1, v2, wins1, wins2)
        
    # Test three of a kind
    if print_tests == True: print("Testing three of a kind.")
    h1_3k = is_n_of_a_kind(v1, 3)
    h2_3k = is_n_of_a_kind(v2, 3)
    if h1_3k and not h2_3k:
        wins1 += 1
        return wins1, wins2 
    elif not h1_3k and h2_3k:
        wins2 += 1
        return wins1, wins2     
    elif h1_3k and h2_3k:
        return play_nkind_tiebreak(v1, v2, wins1, wins2, 3)
    
    # Test two pairs
    if print_tests == True: print("Testing two pairs.")
    h1_2p = is_two_pair(v1)
    h2_2p = is_two_pair(v2)
    if h1_2p and not h2_2p:
        wins1 += 1
        return wins1, wins2 
    elif not h1_2p and h2_2p:
        wins2 += 1
        return wins1, wins2     
    elif h1_2p and h2_2p:
        return play_twopair_tiebreak(v1, v2, wins1, wins2)
    
    # Test two of a kind
    if print_tests == True: print("Testing one pair.")
    h1_2k = is_n_of_a_kind(v1, 2)
    h2_2k = is_n_of_a_kind(v2, 2)
    if h1_2k and not h2_2k:
        wins1 += 1
        return wins1, wins2 
    elif not h1_2k and h2_2k:
        wins2 += 1
        return wins1, wins2     
    elif h1_2k and h2_2k:
        return play_nkind_tiebreak(v1, v2, wins1, wins2, 2)
    
    # Test high card. 
    if print_tests == True: print("Testing highest card.")
    return play_highcard(v1, v2, wins1, wins2)
    
def play_highcard(v1, v2, wins1, wins2):
    """Increment wins solely based on largest value."""
    v1_sorted = sorted(v1, reverse=True)    
    v2_sorted = sorted(v2, reverse=True)    
    if v1_sorted > v2_sorted:
        wins1 += 1
    elif v1_sorted < v2_sorted:
        wins2 += 1
    return wins1, wins2
    
def play_nkind_tiebreak(v1, v2, wins1, wins2, n):
    """Increment in case of a tie break for n of a kind hands."""
    unique_v1, unique_v2 = set(v1), set(v2)
    
    # Extract value of n of a kind for hand 1.
    for uv1 in unique_v1:
        count = 0
        for v in v1:
            if uv1 == v:
                count += 1
        if count == n:
            v1_nk = uv1
            break
    
    # Extract value of n of a kind for hand 2.
    for uv2 in unique_v2:
        count = 0
        for v in v2:
            if uv2 == v:
                count += 1
        if count == n:
            v2_nk = uv2
            break
    
    # Play.
    if v1_nk > v2_nk:
        wins1 += 1
        return wins1, wins2
    elif v1_nk < v2_nk:
        wins2 += 1
        return wins1, wins2
    else:  # Tie
        v1_single = [v for v in v1 if v != uv1]
        v2_single = [v for v in v2 if v != uv2]
        return play_highcard(v1_single, v2_single, wins1, wins2)
    
def play_twopair_tiebreak(v1, v2, wins1, wins2):
    """Increment in case of a tie break for two pair hands."""
    unique_v1, unique_v2 = set(v1), set(v2)
    pairs1, pairs2 = [], []
    # Extract value of pairs for hand 1.
    for uv1 in unique_v1:
        count = 0
        for v in v1:
            if uv1 == v:
                count += 1
        if count == 2:
            pairs1.append(uv1)
    
    # Extract value of pairs for hand 2.
    for uv2 in unique_v2:
        count = 0
        for v in v2:
            if uv2 == v:
                count += 1
        if count == 2:
            pairs2.append(uv2)
    
    # Play.
    v1_max_pair, v1_min_pair = max(pairs1), min(pairs1)
    v2_max_pair, v2_min_pair = max(pairs2), min(pairs2)
    if v1_max_pair > v2_max_pair:
        wins1 += 1
        return wins1, wins2
    elif v1_max_pair < v2_max_pair:
        wins2 += 1
        return wins1, wins2
    else:  # Max pair tied.
        if v1_min_pair > v2_min_pair:
            wins1 += 1
            return wins1, wins2
        elif v1_min_pair < v2_min_pair:
            wins2 += 1
            return wins1, wins2
        else:  # Min pair tied.
            v1_single = [v for v in v1 if v not in pairs1]
            v2_single = [v for v in v2 if v not in pairs2]
            print(v1_single)
            print(v2_single)
            return play_highcard(v1_single, v2_single, wins1, wins2)


start = time.time()

# Get contents of text file as a string.
file = open("p54_poker.txt")
text = file.read()
file.close()

# Process into list of games. Each game consists of two hands.
games = text.split("\n")[:-1]

# Count wins.
wins1, wins2 = 0, 0
for hands in games:
    hands = hands.split(' ')
    h1, h2 = read_hands(hands)
    wins1, wins2 = play(h1, h2, wins1, wins2)
print(wins1, wins2)

print(time.time() - start)


#%%
""" Potential Improvements:
1)  Classify hands as a rank, giving each rank a numerical score. Then compare
    scores.
    
    Extensions / Remarks:
""" 


