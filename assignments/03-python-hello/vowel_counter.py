#!/usr/bin/env python3
"""docstring"""

import os
import sys

arg = sys.argv[1:]
str1 = str(arg)
vowels = 0
 
if len(arg) != 1:
    print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)
arg = arg[0] 


for i in str1:
	if(i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"): 
		vowels=vowels+1
if(vowels==1):
	print('There is {} vowel in "{}."' .format(vowels, arg))
	sys.exit(0)
print('There are {} vowels in "{}."' .format(vowels, arg))
