#!/usr/bin/env python

import sys
from contextlib import closing

import pymysql


with closing(pymysql.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts"
)) as myconn:

    mycursor = myconn.cursor()

    for party in 'Whig', 'Federalist':
        print(party.upper() + ':')

        mycursor.execute('''
        select lname, fname
        from presidents
        where party = %s
        ''', (party,))

        print(mycursor.fetchall())
        print()
        print(mycursor.description)

        # for row in mycursor.fetchall():
        #     print(row)
        # print('-' * 60)
