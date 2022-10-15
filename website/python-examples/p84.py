""" @author: Adam, @date: 8-2-2019 

Monte Carlo simulation. Model playing the game, keeping track of position at 
the end of each turn. 10 million turns in ~1 minute."""

import time 
import random as rand

#%% Monte Carlo solution.

def roll(n):
    """Roll n-sided dice."""
    return rand.randint(1, n)

def n_rolls(n, m):
    """Roll list of n rolls of m-sided die."""
    rolls = []
    for i in range(n):
         rolls.append(roll(m))
    return rolls

def draw_and_replace_card(deck):
    """Draw first card from deck and place in last card of deck. Return
    card and modified deck."""
    card = deck[0]
    return card, deck[1:] + [card]

def ch_action(marker, ch_deck, rr_squares, ut_squares):
    """Draw a chance card and update the marker, placing the card at the
    bottom of the deck and returning the modified marker and deck."""
    card, deck = draw_and_replace_card(ch_deck)
    
    # Update marker
    if card == 'r':  # Go to next railroad square.
        marker = next_rr(marker, rr_squares)
    elif card == 'u': # Go to next utility square.
        marker = next_ut(marker, ut_squares) 
    elif card == 'b':  # Move back 3 squares.
        marker += -3
        marker = marker % 40
    elif card < 0:  # Marker is unchanged.
        return marker, deck
    else:  # To to square card tells you.
        marker = card
    
    return marker, deck

def next_rr(marker, rr_squares):
    """Update marker to next railroad square. """
    for square in rr_squares:
        if marker < square:
            marker = square
            break
    else:
        marker = rr_squares[0]
    
    return marker

def next_ut(marker, ut_squares):
    """Update marker to next utility square. """
    for square in ut_squares:
        if marker < square:
            marker = square
            break
    else:
        marker = ut_squares[0]
    
    return marker

def cc_action(marker, cc_deck):
    """Draw a chance card and update the marker, placing the card at the
    bottom of the deck and returning the modified marker and deck."""
    card, deck = draw_and_replace_card(cc_deck)
    
    # Update marker
    if card < 0:  # Marker is unchanged.
        return marker, deck
    else:  # To to square card tells you.
        marker = card
    
    return marker, deck

    
rand.seed(1)  # Reproducibility.
start_time = time.time()

n_sim = int(1e6)  # Number of Monte Carlo simulations.
n, d = 2, 6  # Number of rolls to make and faces of each die.
marker_dict = {}  # Store times each square is visited.

# Predefine special squares and community/chance cards.
cc_squares = {2, 17, 33}
ch_squares = {7, 22, 36}
g2j_square = {30}
jail_square = {10}
cc_cards = [0, 10] + [-1]*14
ch_cards = [0, 10, 11, 24, 39, 5, 'r', 'r', 'u', 'b'] + [-1]*6
rr_squares = [5, 15, 25, 35]
ut_squares = [12, 28]

# Shuffle cards.
rand.shuffle(cc_cards)
rand.shuffle(ch_cards)

# Start playing.
marker = 0  # Mark which square the player is on.
jail_counter = 0
for i in range(n_sim):
    rolls = n_rolls(n, d)
    
    # If a double is rolled, update jail counter. Otherwise, reset counter.
    if len(set(rolls)) == 1:
        jail_counter += 1
    else:
        jail_counter = 0
        
    # If three doubles are rolled conscecutively, go to jail and reset counter.
    # Otherwise, move forward sum(rolls) steps.    
    if jail_counter == 3:
        marker = 10
        jail_counter = 0
    else:    
        marker += sum(rolls) 
        marker = marker % 40
    
    # Special square actions
    if marker in g2j_square:
        marker = 10
    elif marker in cc_squares:
        marker, cc_cards = cc_action(marker, cc_cards)
    elif marker in ch_squares:
        marker, ch_cards = ch_action(marker, ch_cards, rr_squares, ut_squares)
        if marker in cc_squares:  # Possible if moving backwards 3 from CH3.
            marker, cc_cards = cc_action(marker, cc_cards)
    marker_dict[marker] = marker_dict.get(marker, 0) + 1

# Convert to probabilities and sort results.
results = []
for square, count in marker_dict.items():
    results.append((count/n_sim, square))
results.sort(reverse = True)
print(results)

print(time.time() - start_time)


#%% Comments.
""" Potential improvements: 
    
    Extensions/Remarks:
"""    
                
                
                
                
                
                
                
                
                
                