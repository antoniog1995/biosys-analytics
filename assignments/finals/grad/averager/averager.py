#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Input file(s)',nargs='+')


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
    files = args.FILE
    for file_entry in files:
        l=[]
        n=0
        
        if not os.path.isfile(file_entry):
            print('"{}" is not a file'.format(file_entry),file=sys.stderr)
            continue
        with open(file_entry,"r") as fh:
            for line in fh:
                for i in re.findall(r"[-+]?\d*\.\d+|[+-]?\d+",line):
                    l.append(i) 
            n = len(l)
            if n is 0:
                file_average = 0.00
                print('{:10.02f}: {}'.format(file_average,os.path.basename(file_entry)))
            else:
                l = [float(j) for j in l]
                file_average = sum(l)/n
                print('{:10.02f}: {}'.format(file_average,os.path.basename(file_entry)))
                
            
            
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
