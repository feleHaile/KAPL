#!/usr/bin/python3

import json

with open('../DATA/solar.json') as SOLAR:
    solar = json.load(SOLAR)

for planet in solar['innerplanets']:
    print(planet['name'])

for planet in solar['outerplanets']:
    print(planet['name'])

for planet in solar['dwarfplanets']:
    print(planet['name'])