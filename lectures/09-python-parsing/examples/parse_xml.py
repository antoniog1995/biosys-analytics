#!/usr/bin/env python3
"""
<<<<<<< HEAD
Author : antoniogutierrez-jaramillo
=======
Author : kyclark
>>>>>>> 734e1bfe4c4c271b52422c613503dc51a2fdef9f
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import os
import sys
from xml.etree.ElementTree import ElementTree

<<<<<<< HEAD
=======

>>>>>>> 734e1bfe4c4c271b52422c613503dc51a2fdef9f
# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
<<<<<<< HEAD
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
=======
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
>>>>>>> 734e1bfe4c4c271b52422c613503dc51a2fdef9f
        sys.exit(1)

    file = args[0]

    print('File is "{}"'.format(file))
<<<<<<< HEAD
    
    tree = ElementTree()
    root = tree.parse(file) 
    for key, value in root.attrib.items():
        print('{:13}: {}' .format(key,value))
        
    for id_ in root, find('IDENTIFIERS'):
        print('{:13}: {}'.format(id_,tag,id_,text))
=======

    tree = ElementTree()
    root = tree.parse(file)
    print(type(root.attrib))
    for key, value in root.attrib.items():
        print('{:20}: {}'.format(key, value))

    for id_ in root.find('IDENTIFIERS'):
        print('{:20}: {}'.format(id_.tag, id_.text))

    for attr in root.findall('SAMPLE_ATTRIBUTES/SAMPLE_ATTRIBUTE'):
        print('{:20}: {}'.format(
            attr.find('TAG').text,
            attr.find('VALUE').text))

>>>>>>> 734e1bfe4c4c271b52422c613503dc51a2fdef9f

# --------------------------------------------------
main()
