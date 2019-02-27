#!/usr/bin/env python3
"""docstring"""

import os
import sys

names = sys.argv[1:]

if len(names) == 0:
    print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if len(names) == 1: 
	print('Hello to the 1 of you: '+ names[0]+ '!')
	#print('Hello to the 1 of you: {}!' .format(names))
elif len(names) == 2:
	print('Hello to the 2 of you: {}!' .format(' and ' .join(names)))

elif len(names) > 2:
	num = len(names) 
	print('Hello to the {} of you: {}' .format(num, ', ' .join(names[0:num-1])), end = ', '), print('and {}!' .format(names[num-1]))
names = names[0]

