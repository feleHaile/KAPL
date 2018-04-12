#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

doc = ET.parse('../DATA/solar.xml')

root = doc.getroot()

inner = root.find('solarsystem').find('innerplanets')
outer = root.find('solarsystem').find('outerplanets')

print('Inner:')
for planet in inner:  # loop through children
    print('\t',planet.get("name"))

print('Outer:')
for planet in outer:  # loop through children
    print('\t',planet.get("name"))

