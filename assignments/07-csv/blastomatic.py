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
    
    with open(blast_file) as aFile:
        reader = csv.DictReader(aFile, delimiter='\t') 
        reader.fieldnames = "idnumber","seqid","pident" 
        for row in reader:
            seqid = row['seqid']
            pident =row['pident']
            blast_dict[seqid, pident] = seqid, pident 
    with open(annotation_file) as bFile:
        reader = csv.DictReader(bFile, delimiter=',')
        for row in reader:
            centroid = row['centroid'] 
            genus = row['genus']
            species = row['species']
            annotation_dict[centroid, genus, species] = centroid, genus, species 
    for line in blast_dict:
        for row in annotation_dict:
    	    if row['centroid'] == line['seqid']:
    	        result_dict[centroid, pident, genus, species] = line[seqid], line[pident], row[genus], row[species] 
    	    else: 
    	    	print('Cannot find seq "{}" in lookup'.format(row[centroid]))
    for line in result_dict:
    	print(line) 	    	
    
    	        
    
            
   
    

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
