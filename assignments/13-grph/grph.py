#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-11
Purpose: Rock the Casbah
"""

import argparse
import sys
import os 
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'str', metavar='str', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='K size of overlap',
        metavar='overlap',
        type=int,
        default=3)

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
def find_kmers(s, k):
    kmer_set = []
    n = len(s) - k + 1
    for i in range(0,n):
        kmer_set.append(str(s[i:i+k]))
    #print(kmer_set) 
    return kmer_set 
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    k = args.overlap
    fasta = args.str 
    
    front = {}
    back = {}

    
    if not os.path.isfile(fasta):
        die('"{}" is not a file'.format(fasta))
    with open(fasta, 'r') as sequences:
        for sequence in SeqIO.parse(sequences,"fasta"): 

            key = str(sequence.id) 
            if k <= 0:
                die('-k "{}" must be a positive integer'.format(k)) 
            if len(sequence.seq) < k:
                print('there are no {}-lenght substrings in "{}"'.format(k, sequence))
                sys.exit(0)
            else:
                kmers = find_kmers(sequence.seq,k)
                back[key] = kmers[-1]
                front[key] = kmers[0] 
    #print(back)
    #print(front) 
    
    for entry1,value1 in back.items():
        for entry2, value2 in front.items():
            if entry1 == entry2: 
                continue
            if value1 == value2: 
                print('{} {}'.format(entry1, entry2))
    
    
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
