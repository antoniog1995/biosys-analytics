#!/usr/bin/env python3
"""
Author : antoniog1
Date   : 2019-02-14
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

    parser.add_argument('string', metavar='str', 
                        help='DNA/RNA sequence')
    parser.add_argument('-c', '--codons', help='A file with codon translations',
                        metavar='FILE', type=str, default=None)
    parser.add_argument('-o', '--output', help='Output filename',
                        metavar='FILE', type=str, default='out.txt')

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
    codons = args.codons
    string = args.string
    input_string = string.upper()
    outfile = args.output 
    k = 3 
    n = len(input_string) - k + 1
    
    if codons is None:
        die('usage')
    if not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))
    codonTable = {}
    with open(codons) as cFile:
        for line in cFile:
            inCodon, protein = line.split()
            codonTable[inCodon] = protein
    with open(outfile, 'wt') as out_fh:
        for i in range(0, n, k): 
            inCodon = input_string[i:i+k]
            out_fh.write(codonTable.get(inCodon,'-')) 
    out_fh.close()
    print('Output written to "{}"'.format(outfile)) 
    
    
       

# --------------------------------------------------
if __name__ == '__main__':
    main()
