#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-09
Purpose: Rock the Casbah
"""

import argparse
import sys
import logging 
import os
import random 
import time 



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='FILE inputs', nargs=2)


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

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
    
    
#---------------------------------------------------
def dist(s1, s2):
    diff_count = abs((len(s1) - len(s2)))
    for a,b in zip(s1,s2):
        if a != b:
            diff_count +=1
    return diff_count     
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1,file2 = args.FILE
    debug_flag = args.debug
    dist_count = 0
    #die(type(file1))
    if not os.path.isfile(file1): 
        die('"{}" is not a file'.format(file1))
    if not os.path.isfile(file2):
        die('"{}" is not a file'.format(file2))
    print(debug_flag) 
    
    logging.basicConfig(filename='.log',filemode='w',level=logging.DEBUG if args.debug else logging.CRITICAL)
    
    #if debug_flag is True:
    #    logging.debug('Starting') 
    #    for i in range(1, 11): 
    #        method = random.choice([logging.info, logging.warning, logging.error, logging.critical, logging.debug])
    #        method('{}: Hey!'.format(i))
    #        time.sleep(1)
    #    logging.debug('Done')
    #    print('Done.')  
        
    open1 = open(file1,"r")
    open2 = open(file2,"r") 
    text1 = open1.read().split()
    text2 = open2.read().split()
    #print('{} \n {}'.format(text1,text2))
    #print(text1)
    #print(text2)
    #for word1, word2 in zip(text1, text2): 
    for word1, word2 in zip(text1, text2):
        dist_count += dist(word1, word2) 
    
    
    print(dist_count)


# --------------------------------------------------
if __name__ == '__main__':
    main()
