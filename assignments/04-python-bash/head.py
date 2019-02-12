#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) == 0: 
    print('Usage: head.py FILE [NUM_LINES]') 
    sys.exit(1)
if len(args) < 2:
	num = 3
else: 
	num = int(args[1]) 
if num <= 0: 
	print('lines ({}) must be a positive number' .format(num))
	exit (1) 
if not os.path.isfile(args[0]):
	print('{} is not a file' .format(args[0]))
	sys.exit(1) 
from itertools import islice

with open(args[0]) as myFile:
	for x in range(0, num):
		print(myFile.readline().rstrip())
