#!/usr/bin/env python

# time storage:
#  date or datetime object
#  epoch time (Unix time stamp) seconds since 1/1/70
#  time tuple (9 fields)

from datetime import date
import time


today = date.today()

james_bd = date(2014, 8, 1)

diff = today - james_bd

print("James is {:.2f} years old today".format(
    diff.days/365.25
))

t = time.time()
print(t)
time.sleep(2.5)
t = time.time()
print(t)

