#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-03-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import re 
import dateparser


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'Date', metavar='DATE', help='A positional argument')

    #parser.add_argument(
    #    '-a',
    #    '--arg',
    #    help='A named string argument',
    #    metavar='str',
    #    type=str,
    #    default='')

    #parser.add_argument(
    #    '-i',
    #    '--int',
    #    help='A named integer argument',
    #    metavar='int',
    #    type=int,
    #    default=0)

    #parser.add_argument(
    #    '-f', '--flag', help='A boolean flag', action='store_true')

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
    date = args.Date
    
    month_number_one = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr': '04', 'May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09', 'Oct':'10','Nov':'11','Dec':'12'}
    month_number_two = {'January':'01', 'February':'02', 'March':'03', 'April': '04', 'May':'05','June':'06','July':'07','August':'08','September':'09', 'October':'10','November':'11','December':'12'}
    
    date_re_one = re.compile('(?P<year>\d{4})[-](?P<month>\d{1,2})[-](?P<day>\d{1,2})')
    date_re_two = re.compile('(?P<year>\d{4})[-](?P<month>\d{1,2})')
    date_re_three = re.compile('(?P<year>\d{4})(?P<month>\d{1,2})(?P<day>\d{1,2})')
    date_re_four = re.compile('(?P<month>\w{3,9})[-](?P<year>\d{4})')
    date_re_five = re.compile('(?P<month>\w{3,9})[,][ ](?P<year>\d{4})') 
    date_re_six = re.compile('(?P<month>\d{1,2})[/](?P<year>\d{2})')
    
    match = date_re_one.match(date) or date_re_two.match(date) or date_re_three.match(date) or date_re_four.match(date) or date_re_five.match(date) or date_re_six.match(date) 
    if match is None: 
        die('No match')
    if len(match.group('year')) == 2:
        year = '20' + match.group('year')
    else:
        year = match.group('year') 
    #month = match.group('month') 
    if match.group('month') in month_number_one.keys():
        month = month_number_one[match.group('month')]
    elif match.group('month') in month_number_two.keys():
        month = month_number_two[match.group('month')]
    else:
        month = match.group('month') 
    if len(match.group('month')) == 1:
        month = '0'+match.group('month') 
    
    if date_re_one.match(date) != None or date_re_three.match(date) != None:
        if len(match.group('day')) == 1: 
            day = '0'+match.group('day')
        else:
            day = match.group('day')
    else:
        day = '01' 
    #day = match.group('day') if date_re_one.match(date) != None or date_re_three.match(date) != None else '01'
    
    #if len(match.group('day')) == 1 and day == match.group('day'):
    #    day = '0'+match.group('day')
    print('{}-{}-{}'.format(year,month,day))
        
    
    
            
    





# --------------------------------------------------
if __name__ == '__main__':
    main()
