#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import re 
import os 
from collections import Counter 
from collections import defaultdict 



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='File input(s)', type=argparse.FileType('r', encoding='UTF-8'), nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)


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
    file_handles = args.FILE
    sort_input = args.sort
    min_input = args.min 
    wordcount = defaultdict(int) 
    mod_line = {}
    for file_handle in file_handles:
        for word in file_handle.read().lower().split():
            clean = re.sub('[^a-zA-Z0-9]', '', word)
            if clean:
                wordcount[clean] += 1
        #print(wordcount) 
    if sort_input == "frequency":
        sorted_wordcount = sorted([(x[1],x[0]) for x in wordcount.items()])
        for val, word in sorted_wordcount: 
            if val >= min_input:
                print('{:20} {}'.format(word, val)) 
    else: 
        for word,val in sorted(wordcount.items()):
	        if val >= min_input:
	            print('{:20} {}'.format(word, val))
            
            
                    
                
                
        
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
