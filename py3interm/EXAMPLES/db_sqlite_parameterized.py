#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:

    s3cursor = s3conn.cursor()

    party_query = '''
    select lastname, firstname
    from presidents
    where party = ?
    '''

    for party in 'Federalist', 'Whig':
        print(party)
        s3cursor.execute(party_query, (party,))
        print(s3cursor.fetchall())
        print()

