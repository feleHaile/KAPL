#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

doc = ET.parse('../DATA/solar.xml')

jupiter = doc.find('.//planet[@name="Jupiter"]')

print(jupiter)

for moon in jupiter:
    print(moon.text)
