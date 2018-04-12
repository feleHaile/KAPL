#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

doc = ET.parse('../DATA/solar.xml')

inner_nodes = doc.findall('solarsystem/innerplanets/planet')

outer_nodes = doc.findall('solarsystem/outerplanets/planet')

print('Inner:')
for planet in inner_nodes:  # + outer_nodes:
    print('\t',planet.get("name"))

print('Outer:')
for planet in outer_nodes:  # + outer_nodes:
    print('\t',planet.get("name"))

