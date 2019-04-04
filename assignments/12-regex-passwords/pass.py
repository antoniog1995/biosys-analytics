#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-04
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
        'password', metavar='PASSWORD', help='baseline password')

    parser.add_argument(
       'alternate',
        metavar='ALT',
        help='alternative password')

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
    base_pass = args.password
    alt_pass = args.alternate 
    
    #length = len(base_pass) 
    
    #pass_re = re.compile('(?P<password>\w{len})')
    
    password = base_pass.upper()
    alternate = alt_pass.upper()
    
    match = re.search(password, alternate) 
    if match is not None:
    	print("ok") 
    else: 
        print("nah") 
    
    #alternative = match.group('password')
    #check_password = base_pass.upper() 
    #check_alternative = alt_pass.upper()
    
    #if len(alternative) 
    #if check_alternative == check_password:
    #    print("ok") 
    #else:
    #    print("nah") 

   

# --------------------------------------------------
if __name__ == '__main__':
    main()
