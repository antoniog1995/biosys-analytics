#!/usr/bin/env python3
"""
Author : antoniog1
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO
from collections import Counter

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FASTA', help='Input FASTA file(s)', nargs="+")

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default = 50)

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
    outdir = args.outdir
    percentGClim = args.pct_gc 
    fasta = args.fasta 
    
    i = 1
    gc = 0 
    total = 0
    num_seq = 0
    if percentGClim < 0 or percentGClim > 100:
        die('--pct_gc "{}" must be between 0 and 100'.format(percentGClim))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    for file in fasta:
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file)) 
            continue
        basename,ext = os.path.splitext(os.path.basename(file))
        high_file = basename + '_high' + ext
        low_file = basename + '_low' + ext

        high_path = os.path.join(outdir,high_file)
        low_path = os.path.join(outdir,low_file) 
        
        high_fh = open(high_path, 'wt')
        low_fh = open(low_path, 'wt') 
        
        print("  {}: {}" .format(i,os.path.basename(file)))
        for record in SeqIO.parse(file, 'fasta'):
            seq_len = len(record.seq) 
            nucs = Counter(record.seq) 
            gc_num = nucs.get('G', 0) + nucs.get('C', 0)
            #print(record.seq)
            percentGCact = (gc_num/seq_len)*100
            if percentGCact < percentGClim:
                SeqIO.write(record, low_fh, "fasta") 
                num_seq += 1
            else:
                SeqIO.write(record, high_fh, "fasta")
                num_seq += 1 
        i = i + 1
    print('Done, wrote {} sequences to out dir "{}"'.format(num_seq, outdir))     

# --------------------------------------------------
if __name__ == '__main__':
    main()
