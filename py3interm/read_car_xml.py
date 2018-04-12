#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('cars.xml')

for car in doc.findall('.//car'):
    make = car.get('make')
    year = car.findtext('year')
    model = car.findtext('model')
    print(f"{year} {make:15s} {model}")

