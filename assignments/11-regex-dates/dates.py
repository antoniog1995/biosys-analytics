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
    
    #print(dateparser.parse(date)) 
    if re.match('\d{4}-\d{2}-\d{2}', date) != None:
        date_re = re.compile('(?P<year>\d{4})''[/-]''(?P<month>\d{1,2})''[/-]''(?P<day>\d{1,2})')
        match = date_re.match(date)
        print('{}-{}-{}'.format(match.group('year'),match.group('month'),match.group('day')))

    elif re.match('\d{4}-\d{2}', date) != None:
        date_re = re.compile('(?P<year>\d{4})''[/-]''(?P<month>\d{1,2})')
        match = date_re.match(date)
        print('{}-{}-01'.format(match.group('year'),match.group('month')))
    elif re.match('\d{8}', date) != None:
        date_re = re.compile('(?P<year>\d{4})''(?P<month>\d{1,2})''(?P<day>\d{1,2})')
        match = date_re.match(date)
        print('{}-{}-{}'.format(match.group('year'),match.group('month'),match.group('day'))) 
    elif re.match('\d{1,2}/\d{2}',date) != None:
        date_re = re.compile('(?P<month>\d{1,2})''[/-]''(?P<year>\d{1,2})')
        match = date_re.match(date) 
        if len(match.group('month')) == 1:
            print('20{}-0{}-01'.format(match.group('year'),match.group('month')))
        else:
            print('20{}-{}-01'.format(match.group('year'),match.group('month')))
        #year = data[1] 
        #month = data[0]
        #day = '01' 
        #if len(month) == 1:
        #    print('20{}-0{}-{}'.format(year,month,day))
        #else:
        #    print('20{}-{}-{}'.format(year, month,day)) 
    elif re.match('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)-\d{4}', date) != None:
        date_re = re.compile('(?P<month>\w{2,9})''[/-, ]''(?P<year>\d{4})')
        match = date_re.match(date) 
        
        #data = re.split('-|, ', date)
        #year = data[1]
        #day = '01'
        #month = re.match('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)',date)
        if match.group('month') in month_number_one:
            month_number = month_number_one[match.group('month')]
        elif match.group('month') in month_number_two:
            month_number = month_number_two[match.group('month')]
        else:
            die('unknown month: {}'.format(match.group('month')))
        print('{}-{}-01'.format(match.group('year'),month_number)) 
    elif re.match('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December), \d{4}',date) != None:
        data = re.split('-|, ', date)
        year = data[1]
        day = '01'
        month = re.match('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)',date)
        if month in month_number_one.keys():
            month_number = month_number_one[month]
        elif month in month_number_two:
            month_number = month_number_two[month]
        else:
            die('unknown month: {}'.format(month))
        print('{}-{}-{}'.format(year,month_number,day)) 
    else: 
        print('No match') 
            
    





# --------------------------------------------------
if __name__ == '__main__':
    main()
