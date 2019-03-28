#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-03-21
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-s',
        '--seed',
        help='Random Seed',
        metavar='int',
        type=int,
        default=None)


    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed_number = args.seed
    
    if seed_number is not None:
        random.seed(seed_number) 
    
    unicode_symbols = list('♥♠♣♦')
    a = list('234567890') + list('JQKA')
    deck = sorted(product(unicode_symbols,a))
    random.shuffle(deck) 
    
    n=0
    player_two_score = 0
    player_one_score = 0
    one_value = 0
    two_value = 0 
    
    while n < 52:
        Player_one_card = list.pop(deck) 
        Player_two_card = list.pop(deck) 
        
        
        
        if Player_one_card[1] == '0':
            one_value = 10
        elif Player_one_card[1] == 'J':
            one_value = 11
        elif Player_one_card[1] == 'Q':
            one_value = 12
        elif Player_one_card[1] == 'K':
            one_value = 13
        elif Player_one_card[1] == 'A':
            one_value = 14
        else: 
            one_value = int(Player_one_card[1]) 
             
        if Player_two_card[1] == '0':
            two_value = 10
        elif Player_two_card[1] == 'J':
            two_value = 11
        elif Player_two_card[1] == 'Q':
            two_value = 12
        elif Player_two_card[1] == 'K':
            two_value = 13
        elif Player_two_card[1] == 'A':
            two_value = 14
        else: 
            two_value = int(Player_two_card[1])   
            
        if one_value > two_value:     
            hand_winner = 'P1'
            player_one_score += 1

        elif one_value < two_value:
            hand_winner = 'P2'
            player_two_score +=1
        else:
            hand_winner = 'WAR!'
            
        if Player_one_card[1] == '0':
            print('{}1{}'.format(Player_one_card[0],Player_one_card[1]),end = ' ')
        else: 
            print(' {}{}'.format(Player_one_card[0],Player_one_card[1]),end = ' ')
            
        if Player_two_card[1] == '0':
            print('{}1{}'.format(Player_two_card[0],Player_two_card[1]),end = ' ')
        else:
            print(' {}{}'.format(Player_two_card[0],Player_two_card[1]),end = ' ')
        print('{}'.format(hand_winner))
        n += 2
    if player_two_score > player_one_score:
        winner = 'Player 2 wins' 
    elif player_two_score < player_one_score: 
        winner = 'Player 1 wins'
    else:
        winner = 'DRAW' 
    print('P1 {} P2 {}: {}'.format(player_one_score, player_two_score, winner)) 
     
     


# --------------------------------------------------
if __name__ == '__main__':
    main()
