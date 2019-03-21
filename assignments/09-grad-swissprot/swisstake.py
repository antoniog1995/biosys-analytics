#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import os 
from Bio import SeqIO 
from Bio import SwissProt 

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        'FILE', 
        help='Uniprot file', 
        metavar='FILE')
        
    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs ='+',
        default='')
            
    parser.add_argument(
        '-k',
        '--keyword',
        metavar='STR', 
        help='Take on keyword', 
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default="out.fa")



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
    
    uniprot = args.FILE
    keyword = args.keyword.capitalize() 
    skips = args.skip
    output = args.output 
    skip_number = 0
    key_number = 0 
    skip_set = set(skips) 
    
    
    if not os.path.isfile(uniprot): 
        die('"{}" is not a file'.format(uniprot))
        
    print('Processing "{}"'.format(uniprot))
    outfile = open(output,'wt') 
    
    skip_number = 0
    line_number = 0 
    with open(uniprot) as file:
        for record in SeqIO.parse(file,"swiss"):
            #print(record)
            taxa = record.annotations["taxonomy"]
            #print(taxa) 
            for line in record.annotations["keywords"]: 
                if any([a for a in map(str.upper, skips) if a in map(str.upper, taxa)]) == True: 
                #for skip in skips:
                #    skip.lower().capitalize()
                #    if skip in record.annotations["taxonomy"]:
                        #print([a for a in map(str.upper, skips) if a in map(str.upper, taxa)])
                        skip_number += 1
                        break
                if keyword == line: 
                    #print(line) 
                    SeqIO.write(record, output, "fasta")
                    key_number += 1
   
    outfile.close()
    print('Done, skipped {} and took {}. See output in "{}".'.format(skip_number, key_number, output)) 
                 
            
        
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
