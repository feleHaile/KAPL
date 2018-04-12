#!/usr/bin/env python

from distutils.core import setup, Extension

module1 = Extension('john',
                    sources = ['johnmodule.c'])

setup (name = 'John',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])

# note:
# for Windows may need to create c:\python27\lib\distutils\distutils.cfg and put the following in it:
# [build]
# compiler=mingw32