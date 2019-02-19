#!/usr/bin/env python3
"""
Author : antoniog1
Date   : 2019-02-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional', metavar='STATE', help='A positional argument')

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
    state = args.positional
    j = 1

    for i in state:

        if i not in '.XO' or len(state) != 9:
            die('State "{}" must be 9 characters of only ., X, O'.format(state)) 
   
    if state[0:3] == 'XXX' or state[3:6] == 'XXX' or state[6:9] == 'XXX':
        die('X has won')  
    if state[0:9:3] == 'XXX' or state[1:9:3] == 'XXX' or state[2:9:3] == 'XXX':
        die('X has won') 
    if state[0:9:4] == 'XXX' or state[2:7:2] == 'XXX': 
        die('X has won') 
   
    if state[0:3] == 'OOO' or state[3:6] == 'OOO' or state[6:9] == 'OOO':
        die('O has won') 
    if state[0:9:3] == 'OOO' or state[1:9:3] == 'OOO' or state[2:9:3] == 'OOO':
        die('O has won') 
    if state[0:9:4] == 'OOO' or state[2:7:2] == 'OOO':
        die('O has won') 
    print('No winner') 
    
  
# --------------------------------------------------
if __name__ == '__main__':
    main()
