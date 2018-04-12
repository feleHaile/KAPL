#!/usr/bin/env python
import lxml.etree as ET
# import xml.etree.ElementTree as ET

car_data = [
    ('Toyota', 'Corolla', 2001),
    ('Jeep', 'CJ-5', 1970),
    ('BMW', '325xi', 2005),
    ('Lamborghini', 'Youcantaffordit', 1992),
]

root = ET.Element("cars")
for make, model, year in car_data:
    car = ET.SubElement(root, 'car', make=make)
    ET.SubElement(car, 'model').text = model
    ET.SubElement(car, 'year').text = str(year)

print(ET.tostring(root, pretty_print=True).decode())

doc = ET.ElementTree(root)
doc.write('cars.xml', pretty_print=True, xml_declaration=True)
