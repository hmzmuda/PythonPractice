import numpy as np
import math as mt


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_1_score = helping_hand(hand_1)
    hand_2_score = helping_hand(hand_2)
    
    if hand_1_score <= 21:
        if hand_1_score > hand_2_score:
            return True
    else:
        return False
    

def helping_hand(hand):
    hand_score = 0
    ace_score = 0
    for card in hand:
        if card in ['J','K','Q']:
            hand_score += 10
        elif card == 'A':
            ace_score += 1
        else:
            hand_score += int (card)
    hand_score += ace_score
    if hand_score + (10 * ace_score) <= 21 and ace_score > 0:
        hand_score += (ace_score * 10)
        return hand_score
    else:
        return hand_score

blackjack_hand_greater_than(['J','A', '5'], ['6', 'K', 'A'])
