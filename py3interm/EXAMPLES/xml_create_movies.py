#!/usr/bin/python3
from xml.etree import ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            
root = ET.Element('movies')

for m in ('Superman Returns','This is Spinal Tap'):
    me = ET.Element('movie')
    me.text = m
    root.append(me)

movie1 = ET.Element('movie', director='Spielberg, Stephen')
root.append(movie1)
movie1.text = 'Jaws'

movie2 = ET.Element('movie',director='Hitchcock, Alfred')
movie2.text = 'Vertigo'
actor1 = ET.Element('actor')
actor1.text = 'James Stewart'
movie2.append(actor1)
actor2 = ET.Element('actor')
actor2.text = 'Kim Novak'
movie2.append(actor2)
root.append(movie2)

movie3 = ET.Element('movie',director='Welles, Orson')
movie3.text = 'Citizen Kane'
root.append(movie3)

indent(root)  # prettyprint -- optional

doc = ET.ElementTree(root)

doc.write('movies.xml')

