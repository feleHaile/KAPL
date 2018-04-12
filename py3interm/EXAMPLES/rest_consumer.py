#!/usr/bin/python3
import sys

import urllib.request, urllib.error, urllib.parse
import json

header_types = (
    'text/html',
    'text/plain',
    'application/json',
    'application/xml',
)

for header_type in header_types:
	r = urllib.request.Request(
	    'http://localhost:8080/presidents/40',
	    headers={'accept':header_type}
	)
	
	svc = urllib.request.urlopen(r)
	result = svc.read()
	print("{0}\n{1}\n{0}:\n{2}\n".format('*' * 30,header_type,result))
