#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-02-28
Purpose: Rock the Casbah
"""

import argparse
import sys
import os 
import csv 

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='BLAST output')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    blast_file = args.FILE
    annotation_file = args.annotations
    outfile = args.outfile 
    
    blast_dict = {}
    annotation_dict = {}
    result_dict = {}
    
     
    if not os.path.isfile(blast_file):
     	die('"{}" is not a file'.format(blast_file))
    if not os.path.isfile(annotation_file):
        die('"{}" is not a file'.format(annotation_file))
    
    lookup = {}
    with open(annotation_file) as bFile:
        reader = csv.DictReader(bFile, delimiter=',')
        for row in reader:
            lookup[row['centroid']]=row 
    blastfields = ['qacver','saccver','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
    
    out_fh = open(outfile, 'wt') if outfile else sys.stdout
    out_fh.write('\t'.join(['seqid','pident','genus','species']) + '\n')
    
            #centroid = row['centroid'] 
            #genus = row['genus']
            #if genus == "":
                #genus == "NA"
            #species = row['species']
            #if species == "":
                #species == "NA"
            #keypoint = (genus,species)
            #annotation_dict[centroid] = keypoint  
    with open(blast_file) as aFile:
        reader = csv.DictReader(aFile, delimiter='\t', fieldnames = blastfields)
        #reader.fieldnames = "qacver","saccver","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"
        for row in reader:
            seqid = row['saccver']
            if seqid not in lookup:
                warn('Cannot find seq "" in lookup'.format(seqid))
                continue
        	    
            info = lookup[seqid]
            out_fh.write('\t'.join([row['saccver'],row['pident'],info['genus'] or 'NA',info['species'] or 'NA']) + '\n') 
    out_fh.close 
            #for line in annotation_dict:
                #if line[0] == row['qacver']:
                    #print('{}\t{}'.format(row['qacver'], row['pident']), end ="\t")
                    #print('{}\t{}'.format(line[1]))
                    
                    #break
                #else:
                    #warn('Cannot find seq "" in lookup'.format(line[0]))
                    #break
            
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
