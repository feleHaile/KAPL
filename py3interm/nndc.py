#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://www.nndc.bnl.gov/nsr/"

w = webdriver.Chrome()

w.get(URL)

nuc = w.find_element_by_name('nuc')

print(nuc)

nuc.send_keys('1H')
nuc.send_keys(Keys.ENTER)

for tag in w.find_elements_by_name('exper'):
    if tag.get_attribute('value') == 'yes':
        tag.click()
        break
else:
    print("Button not found!")

