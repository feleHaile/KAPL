
import json
from pprint import pprint

with open('../DATA/solar.json') as SOLAR:
    solar = json.load(SOLAR)

# json.loads(STRING)
# json.load(FILE_OBJECT)
    
pprint(solar)
print()

print(solar['innerplanets'])
print('*' * 60)
print(solar['innerplanets'][0]['name'])
print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets']:
    print(planet['name'])

print("*" * 60)
for group in solar:
    if group.endswith('planets'):
        for planet in solar[group]:
            print(planet['name'])
