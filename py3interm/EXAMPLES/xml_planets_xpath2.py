#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

doc = ET.parse('../DATA/solar.xml')

jupiter = doc.findall('.//planet[@name="Jupiter"]')

for moon in jupiter[0]:
    print(moon.text)  # grab attribute
