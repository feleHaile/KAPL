#!/usr/bin/python3

import sys

class Thing(object):
    def __init__(self,magic_word='poof'):
        self.magic_word = magic_word
    
    def __enter__(self):
        print("Entering context")
        return self
        
    def __exit__(self,objtype,value,traceback):
        print("Exiting context")
        print("Magic word is",self.magic_word,end="\n\n")
        return True
    
with Thing() as t:
    print("in the middle")
    
with Thing('aardvark') as t:
    print("in the middle, earth-pig")
