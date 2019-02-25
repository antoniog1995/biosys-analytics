#!/usr/bin/env python3
"""
Author : antoniog1
Date   : 2019-02-21
Purpose: Rock the Casbah
"""

import argparse
import sys
import os 

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional', metavar='DIR', type = str, help='A positional argument', nargs="+")

    parser.add_argument('-w', '--width', help='A named integer argument', metavar='int', type=int, default=50)

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
    width = args.width
    directory = args.positional    

    for dir_name in directory:
        dir_dict = {}
        if not os.path.isdir(dir_name):
            warn('"{}" is not a directory'.format(dir_name))
            continue
        print(dir_name) 
        for filename in os.listdir(dir_name):            
            path = os.path.join(dir_name,filename)
            with open(path) as f:
                first_line = f.readline().rstrip()
                dir_dict[first_line] = filename
        for line, file in sorted(dir_dict.items()):
            num_per = width - len(line) - len(file) 
            ellipses = "." * num_per
            print('{} {} {}'.format(line,ellipses,file))
# --------------------------------------------------
if __name__ == '__main__':
    main()
