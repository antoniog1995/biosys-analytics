#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-25
Purpose: Rock the Casbah
"""

import argparse
import sys
from tabulate import tabulate
import re
import os 
import logging 
import io 
from itertools import product


# --------------------------------------------------

def dist(s1, s2):
    diff_count = abs((len(s1) - len(s2)))
    for a,b in zip(s1,s2):
        if a != b:
            diff_count +=1
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2,diff_count))
    return diff_count     
# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n
        
# --------------------------------------------------
def uniq_words(file, min_len): 
    word_set = set([])
    for word in file.read().lower().split(): 
        clean = re.sub('[^a-zA-Z0-9]', '', word)
        if clean:
            if len(clean) >= min_len: 
                word_set.add(clean) 
    return word_set
    
# --------------------------------------------------	
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])    
# --------------------------------------------------

def common(words1, words2, distance):
    common_words = list() 
    for s1, s2 in sorted(product(words1, words2)):
        dist_count = dist(s1, s2) 
        #print(dist_count)
        if dist_count <= distance:
            word_tuple = (s1, s2, dist_count)
            common_words.append(word_tuple)
    return common_words 
# --------------------------------------------------
    
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]    

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Input files', nargs=2, type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)
        
    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming Distance',
        metavar='int',
        type=int,
        default=0)
        
    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')
        
    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true',default=False)
        
    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true',default=False)
    

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
    fh1,fh2 = args.FILE
    min_length = args.min_len
    hamming_dist = args.hamming_distance
    logfile_output=args.logfile 
    debug_flag = args.debug
    table_flag = args.table
    headers = ["word1", "word2", "distance"]
    
    logging.basicConfig(filename=logfile_output, filemode='w', level=logging.DEBUG if args.debug else logging.CRITICAL)
    logging.debug('fh1 = {}, fh2 = {}'.format(fh1,fh2))
    
    if hamming_dist < 0:
        die('--distance "{}" must be > 0'.format(hamming_dist))
    words1 = uniq_words(fh1, min_length)
    words2 = uniq_words(fh2, min_length) 
    common_words = common(words1, words2, hamming_dist)
    #print(common_words) 
    if common_words == []: 
        print("No words in common.") 
    else:
        if table_flag == True: 
            print(tabulate(common_words,headers, tablefmt="psql" ))    
        else: 
        #print(common_words, sep='\t')
            print('{}\t{}\t{}'.format(headers[0],headers[1],headers[2]), sep = '\t')
            for entry in common_words:
                print(entry[0],entry[1],entry[2],sep="\t")
    
    
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
