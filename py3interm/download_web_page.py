#!/usr/bin/env python
from urllib import request
import os

URL = "https://navalnuclearlab.energy.gov/"

response = request.urlopen(URL)

print(response.info())

page = response.read()

print(page.decode())

PDF_URL = "https://navalnuclearlab.energy.gov/ckfinder/userfiles/files/Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype(3).pdf"

response = request.urlopen(PDF_URL)

pdf_data = response.read()

with open('nnl.pdf', 'wb') as nnl_out:
    nnl_out.write(pdf_data)

os.system('open nnl.pdf')
