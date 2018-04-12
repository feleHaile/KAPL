#!/usr/bin/python

def pres_upper():
    with open('../DATA/presidents.txt') as PRES:
        for line in PRES:
            (
                 term,lname,fname,
                 bdate, ddate,
                 bplace,bstate,
                 tsdate, tedate,
                 party
            )  = line[:-1].split(':')

            yield '{0} {1}'.format(fname,lname).upper()

    PRES.close()

for p in pres_upper():
    print(p)
    
    
