#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-03-14
Purpose: Rock the Casbah
"""


import sys
import os 
from xml.etree.ElementTree import ElementTree


# --------------------------------------------------

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
    args = sys.argv[1:]
    if len(args) != 1
        print('Usage: {} FILE'.format.(os.path.basename(sys.argv[0])))
        sys.exit(1) 
    
    file = args[0]
    
    tree = ElementTree()
    root = tree.parse(file) 
    for key, value in root.attrib.items()
        print('{:13}: {}'.format(key,value))
        
    for id_ in root.find('IDENTIFIERS'):
        print('{:13}: {}'.format(id_,tag, id_,text))
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
