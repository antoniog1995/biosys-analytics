#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-03-12
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

    
    parser.add_argument(
        '-n INT',
        '--num_bottles',
        help='A named integer argument',
        metavar='INT',
        type=int,
        default=10)

 
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
    bottlenum = args.num_bottles 
    
    bottledown = bottlenum - 1
    if bottlenum < 1:
        die('N ({}) must be a positive integer'.format(bottlenum))
    while bottlenum >= 1:
        if bottlenum == 1:
            print('{} bottle of beer on the wall,'.format(bottlenum))
            print('{} bottle of beer,'.format(bottlenum)) 
        else:
            print('{} bottles of beer on the wall,'.format(bottlenum))
            print('{} bottles of beer,'.format(bottlenum))
        print('Take one down, pass it around,')
        if bottledown == 1:
            print('{} bottle of beer on the wall!'.format(bottledown))
            print('') 
        else:
            if bottledown == 0: 
                print('{} bottles of beer on the wall!'.format(bottledown))
            else:
                print('{} bottles of beer on the wall!'.format(bottledown))
                print('')  
        bottlenum -= 1
        bottledown -= 1

# --------------------------------------------------
if __name__ == '__main__':
    main()
