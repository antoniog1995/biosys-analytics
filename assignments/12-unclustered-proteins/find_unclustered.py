#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-04
Purpose: Rock the Casbah
"""

import argparse
import sys
from Bio import SeqIO
import os
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True)
    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,required=True)
    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    cdhit = args.cdhit
    proteins = args.proteins
    output = args.outfile 
    cluster_set = set()
    write_count = 0
    count = 0

    cluster_search = re.compile('[>]gi[|](?P<numbers>\d+)') 
    fasta_search = re.compile('[>](?P<ID>\d+)')

    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))
    if not os.path.isfile(cdhit):
    	die('--cdhit "{}" is not a file'.format(cdhit))
    	
    outfile = open(output, "w")
    
    with open(cdhit) as cdfile: 
        for line in cdfile: 
            match = cluster_search.search(line)
            if match is None:
                continue 
            search_sequence = match.group('numbers')
            cluster_set.add(search_sequence)
    with open(proteins) as protein_file:
        for line in protein_file:
            match = fasta_search.search(line) 
            if match is None: 
                continue 
            line_sequence = match.group('ID') 
            if line_sequence not in cluster_set: 
                outfile.write(line)
                write_count +=1
            count += 1 
    outfile.close()
    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(write_count, count, output))
    
            
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
