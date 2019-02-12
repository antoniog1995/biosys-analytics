#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    	print('Usage: cat_n.py FILE')
    	sys.exit(1)
if not os.path.isfile(args[0]):
	print('{} is not a file' .format(args[0]))
	sys.exit(1)
pathway = str(args[0])
with open(pathway) as pw:
	line = pw.readline()
	num = 1
	while line: 
		if num < 10: 
			print('     {}: {}' .format(num,line.strip()))
			line = pw.readline()
			num += 1	  
		else:
			print('    {}: {}' .format(num, line.strip()))
			line = pw.readline()
			num += 1


