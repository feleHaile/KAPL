#!/usr/bin/python3
import sys
import sqlite3

myconn = sqlite3.connect("../DATA/PRESIDENTS")

c = myconn.cursor()

c.execute('select fname,lname,birthstate from presidents')
for x in sorted(c.fetchall(),key=lambda e: (e[2],e[1],e[0])):
    print("{0[2]:20} {0[0]} {0[1]}".format(x))

c.execute('select distinct birthstate from presidents')
states = (e[0] for e in c.fetchall())
print(",".join(sorted(states)))
    
c.close()
myconn.close()

