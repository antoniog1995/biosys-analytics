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
        help='seed for random number generator',
        metavar='int',
        type=int,
        default = None)
    parser.add_argument(
        '-p', '--player_hits', help = 'player flag', action='store_true')
    parser.add_argument(
        '-d', '--dealer_hits', help='dealer flag', action='store_true')

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
    player = args.player_hits
    dealer = args.dealer_hits
    
    if seed_number is not None:
        random.seed(seed_number)
        
    #unicode_symbols = list('♥♠♣♦')
    #a = list('234567890') + list('JQKA')
    #deck = sorted(product(unicode_symbols,a))
    #random.shuffle(deck) 
    
    unicode_symbols = list('♥♠♣♦')
    a = list('A234567890JQK') 
    deck = sorted(product(unicode_symbols,a))
    random.shuffle(deck)  
    
    n = 0
    player_score = 0
    dealer_score = 0
    
    player_one = 0
    player_two = 0
    player_three = 0
    
    dealer_one = 0
    dealer_two = 0
    dealer_three = 0
    
    player_one_value = 0
    player_two_value = 0
    player_three_value = 0 
    
    dealer_one_value = 0
    dealer_two_value = 0 
    dealer_three_value = 0 
    
    player_one = list.pop(deck) 
    if player_one[1] == 'A':
        player_one_value = 1
    elif player_one[1] == '0':
        player_one_value = 10
    elif player_one[1] == 'J' or player_one[1] == 'K' or player_one[1] == 'Q':
        player_one_value = 10
    else:
        player_one_value = int(player_one[1])
        
    dealer_one = list.pop(deck) 
    if dealer_one[1] == 'A':
        dealer_one_value = 1
    elif dealer_one[1] == '0':
        dealer_one_value = 10
    elif dealer_one[1] == 'J' or dealer_one[1] == 'K' or dealer_one[1] == 'Q':
        dealer_one_value = 10
    else:
        dealer_one_value = int(dealer_one[1])  
          
    player_two = list.pop(deck)
    if player_two[1] == 'A':
        player_two_value = 1
    elif player_two[1] == '0':
        player_two_value = 10
    elif player_two[1] == 'J' or player_two[1] == 'K' or player_two[1] == 'Q':
        player_two_value = 10
    else:
        player_two_value = int(player_two[1])
        
    dealer_two = list.pop(deck)
    if dealer_two[1] == 'A':
        dealer_two_value = 1
    elif dealer_two[1] == '0':
        dealer_two_value = 10
    elif dealer_two[1] == 'J' or dealer_two[1] == 'K' or dealer_two[1] == 'Q':
        dealer_two_value = 10
    else:
        dealer_two_value = int(dealer_two[1])  
    
    
    if player == True: 
        player_three = list.pop(deck)
        if player_three[1] == 'A':
            player_three_value = 1
        elif player_three[1] == '0':
            player_three_value = 10
        elif player_three[1] == 'J' or player_three[1] == 'K' or player_three[1] == 'Q':
            player_three_value = 10
        else:
            player_three_value = int(player_three[1])
        
        
    if dealer == True:
        dealer_three = list.pop(deck) 
        if dealer_three[1] == 'A':
            dealer_three_value = 1
        elif dealer_three[1] == '0':
            dealer_three_value = 10
        elif dealer_three[1] == 'J' or dealer_three[1] == 'K' or dealer_three[1] == 'Q':
            dealer_three_value = 10
        else:
            dealer_three_value = int(dealer_three[1])
            
    player_score = player_one_value + player_two_value + player_three_value 
    dealer_score = dealer_one_value + dealer_two_value + dealer_three_value 
    
  
    if dealer_score < 10:
        print('D [ {}]:'.format(dealer_score),end=' ')
    else:
        print('D [{}]:'.format(dealer_score),end=' ')
    
    if dealer_one[1] == '0':
        print('{}{}'.format(dealer_one[0],'10'),end=' ')
    else:
        print('{}{}'.format(dealer_one[0],dealer_one[1]),end = ' ')
    #if dealer_two[1] == '0':
    #    print('{}{}'.format(dealer_two[0],'10'),end='') 
    #else:
    #    print('{}{}'.format(dealer_two[0],dealer_two[1]),end = '')
        
    if dealer == True:
        if dealer_two[1] == '0':
            print('{}{}'.format(dealer_two[0],'10'),end='') 
        else:
            print('{}{}'.format(dealer_two[0],dealer_two[1]),end = '')
        if dealer_three[1] == '0':
            print(' {}{}'.format(dealer_three[0],'10'))
        else:
            print(' {}{}'.format(dealer_three[0],dealer_three[1]))
    else:  
        if dealer_two[1] == '0':
            print('{}{}'.format(dealer_two[0],'10')) 
        else:
            print('{}{}'.format(dealer_two[0],dealer_two[1]))
        
    if player_score < 10:
        print('P [ {}]:'.format(player_score),end=' ')
    else:
        print('P [{}]:'.format(player_score),end=' ')
    
    if player_one[1] == '0':
        print('{}{}'.format(player_one[0],'10'),end=' ') 
    else:
        print('{}{}'.format(player_one[0],player_one[1]),end = ' ')
    #if player_two[1] == '0':
    #    print('{}{}'.format(player_two[0],'10'),end='') 
    #else:
    #    print('{}{}'.format(player_two[0],player_two[1]),end = '')
        
    if player == True:
        if player_two[1] == '0':
            print('{}{}'.format(player_two[0],'10'), end = '') 
        else:
            print('{}{}'.format(player_two[0],player_two[1]),end = '')
        if player_three[1] == '0':
            print(' {}{}'.format(player_three[0],'10')) 
        else:
            print(' {}{}'.format(player_three[0],player_three[1]))
    else: 
        if player_two[1] == '0':
            print('{}{}'.format(player_two[0],'10')) 
        else:
            print('{}{}'.format(player_two[0],player_two[1]))
        #if player_three[1] == '0':
        #    print(' {}{}'.format(player_three[0],'10')) 
        #else:
        #    print(' {}{}'.format(player_three[0],player_three[1]))
        
    
    if player_score > 21:
        print('Player busts! You lose, loser!') 
        sys.exit(0) 
    if dealer_score > 21:
        print('Dealer busts.')
        sys.exit(0) 
    if player_score == 21:
        print('Player wins. You probably cheated.') 
        sys.exit(0) 
    if dealer_score == 21:
        print('Dealer wins!') 
        sys.exit(0) 
    
    if dealer_score < 18:
        print('Dealer should hit.') 
    if player_score < 18:
        print('Player should hit.')   
              
          
  
    

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
