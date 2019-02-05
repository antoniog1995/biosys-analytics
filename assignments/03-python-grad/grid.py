#!/usr/bin/env python3
"""docstring"""

import os
import sys

arg = sys.argv[1:] 

if len(arg) != 1:
    print("Usage: grid.py NUM ")
    sys.exit(1)
NUM = int(arg[0]) 
if NUM <= 1 or NUM >= 10:
	print('NUM ({}) must be between 1 and 9' .format(NUM))
	exit(1) 
max = NUM ** 2
for i in range(max):
	i=i+1
	if i < 10:	
		print("  {}" .format(i), end = "") 
	if i >= 10: 
		print(" {}" .format(i), end = "")
	if i%NUM==0:
		print("")
arg = arg[0] 
