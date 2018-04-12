#!/usr/bin/env python
import requests
import os
from pprint import pprint

URL = "https://navalnuclearlab.energy.gov/"

response = requests.get(URL)

pprint(response.headers)
print('-' * 60)

page = response.content

print(page.decode())

PDF_URL = "https://navalnuclearlab.energy.gov/ckfinder/userfiles/files/Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype(3).pdf"

response = requests.get(
    PDF_URL,
    # proxy={'https': 'blah.nnl.gov'},
    # auth=('jstrick', 'l0l'),
    # data={'name':'Bob'},
    # params={'x':5, 'y': 4},
)

pdf_data = response.content

with open('nnl.pdf', 'wb') as nnl_out:
    nnl_out.write(pdf_data)

os.system('open nnl.pdf')
