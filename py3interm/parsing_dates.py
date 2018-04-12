#!/usr/bin/env python
from datetime import datetime
from dateutil.parser import parse

james_bd = '2014-08-01'

d1 = datetime.strptime(james_bd, '%Y-%m-%d')
print(d1)
d2 = parse(james_bd)
print(d2)
year, month, day = james_bd.split('-')
d3 = datetime(int(year), int(month), int(day))
print(d3)

for date_str in ('Apr 1 1970', 'Apr 1, 1970', "Apr 1, '70",
    '4/1/70', 'April 1st, 1970', '1 Apr 1970', 'APRIL 1, 1970'):
    print(parse(date_str))

#  2/4/69  4/2/69
