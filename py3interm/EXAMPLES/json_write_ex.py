#!/usr/bin/python3

import json

george = [{
    'num':1,
    'lname':'Washington',
    'fname':'George',
    'dstart':[1789,4,30],
    'dend':[1797,3,4],
    'birthplace':'Westmoreland County',
    'birthstate':'Virginia',
    'dbirth':[1732,2,22],
    'ddeath':[1799,12,14],
    'assassinated': False,
    'party':'no party',
},{'foo':'bar'}]

js = json.dumps(george,indent=8)
print(js)

with open('george.json','w') as JS:
    json.dump(george,JS)