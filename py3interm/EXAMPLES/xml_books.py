#!/usr/bin/python3

from xml.etree import ElementTree as ET

def fetch_marc_subfield(marcrec,tag,code):
    for datafield in marcrec.findall('datafield'):
        if datafield.get('tag') == tag:
            for subfield in datafield.findall('subfield'):
                if subfield.get('code') == code:
                    return subfield.text

bookroot = ET.parse('../DATA/books.xml')

for num,rec in enumerate(bookroot.getiterator('record')):
    print("Record:",num+1)
    print("\tAuthor:",fetch_marc_subfield(rec,'100','a'))
    print("\tTitle:",fetch_marc_subfield(rec,'245','a'))
    print("\tISBN:",fetch_marc_subfield(rec,'020','a'))
    
