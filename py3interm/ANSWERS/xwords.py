#!/usr/bin/python 

import xml.etree.ElementTree as ET

WORDS = open('../DATA/words.txt')
xwords = [ word[:-1] for word in WORDS if word.startswith('x') ]
WORDS.close()

root = ET.Element('words')
for word in xwords:
    word_element = ET.Element('word')
    word_element.text = word 
    root.append(word_element)

tree = ET.ElementTree(root)
tree.write('xwords.xml')
