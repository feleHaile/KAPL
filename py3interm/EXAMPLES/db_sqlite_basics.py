#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:

    s3cursor = s3conn.cursor()

    # select first name, last name from all presidents
    s3cursor.execute('''
        select firstname, lastname
        from presidents
    ''')

    print("Sqlite3 does not provide a row count\n")
    
    for row in s3cursor.fetchall():
        print(' '.join(row))
    # note -- Sqlite3 does not return the number of rows
    print()



