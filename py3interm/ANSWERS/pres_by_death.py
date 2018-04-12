#!/usr/bin/python
import datetime

info = []
with open('../DATA/presidents.txt') as PRES:
    for line in PRES:
        (
            term, lname, fname, bdate, ddate, bplace, bstate, tsdate, tedate, party
        ) = line[:-1].split(':')

        name = '{0} {1}'.format(fname,lname)

        # strptime converts to datetime
        if ddate != 'NONE':
            deathdate = datetime.datetime.strptime(ddate,'%Y-%m-%d')
        else:
            deathdate = datetime.datetime.now()

        deathdate = deathdate.date()  # convert datetime to date

        info.append( (name, deathdate, party ) )

for name, date, party in sorted(info, key=lambda e: e[1]):
    print("{0:35s} {1} {2}".format(name, date, party))
    
    
