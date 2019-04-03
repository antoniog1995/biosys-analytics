#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'State', metavar='STATE', help='A positional argument')

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
    state = args.State
    
    good_re = re.compile('[XO.]{9}')
    match = good_re.match(state)
    
    x_win_one = re.compile('[X]{3}[.OX]{6}')
    x_win_two = re.compile('[.OX]{3}[X]{3}[.OX]{3}') 
    x_win_three = re.compile('[.OX]{6}[X]{3}') 
    x_win_four = re.compile('[X]{1}[.XO]{2}[X]{1}[.OX]{2}[X]{1}[.XO]{2}')
    x_win_five = re.compile('[.OX]{1}[X]{1}[.OX]{2}[X]{1}[.OX]{2}[X]{1}[.OX]{1}')
    x_win_six = re.compile('[.OX]{2}[X]{1}[.OX]{2}[X]{1}[.XO]{2}[X]{1}')
    x_win_seven = re.compile('[X]{1}[.OX]{3}[X]{1}[.XO]{3}[X]{1}')
    x_win_eight = re.compile('[.OX]{2}[X]{1}[.XO]{1}[X]{1}[X.O]{1}[X]{1}[.XO]{2}') 
    
    o_win_one = re.compile('[O]{3}[.XO]{6}')
    o_win_two = re.compile('[.OX]{3}[O]{3}[.OX]{3}') 
    o_win_three = re.compile('[.OX]{6}[O]{3}') 
    o_win_four = re.compile('[O]{1}[.OX]{2}[O]{1}[.XO]{2}[O]{1}[.XO]{2}')
    o_win_five = re.compile('[.XO]{1}[O]{1}[.OX]{2}[O]{1}[.OX]{2}[O]{1}[O.X]{1}')
    o_win_six = re.compile('[.XO]{2}[O]{1}[.OX]{2}[O]{1}[.XO]{2}[O]{1}')
    o_win_seven = re.compile('[O]{1}[.XO]{3}[O]{1}[.OX]{3}[O]{1}')
    o_win_eight = re.compile('[.OX]{2}[O]{1}[.XO]{1}[O]{1}[.XO]{1}[O]{1}[.OO]{2}')
    
    
    if match is None:
        die('State "{}" must be 9 characters of only ., X, O'.format(state))
    X_board_state = x_win_one.match(state) or x_win_two.match(state) or x_win_three.match(state) or x_win_four.match(state) or x_win_five.match(state) or x_win_six.match(state) or x_win_seven.match(state) or x_win_eight.match(state)
    O_board_state = o_win_one.match(state) or o_win_two.match(state) or o_win_three.match(state) or o_win_four.match(state) or o_win_five.match(state) or o_win_six.match(state) or o_win_seven.match(state) or o_win_eight.match(state)
    if X_board_state is not None:
    	print('X has won')
    	sys.exit(0)
    if O_board_state is not None:
        print('O has won')
        sys.exit(0)
    print('No winner')             


# --------------------------------------------------
if __name__ == '__main__':
    main()
    
