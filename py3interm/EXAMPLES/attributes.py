#!/usr/bin/python3

class Spam(object):
    
    def eggs(self,msg):
        print("eggs!",msg)
        
s = Spam()

s.eggs("fried")

print("hasattr()",hasattr(s,'eggs'))
e  = getattr(s,'eggs')
e("scrambled")

def toast(self,msg):
    print("toast!",msg)
    
setattr(Spam,'eggs',toast)

s.eggs("buttered!")

delattr(Spam,'eggs')

try:
    s.eggs("shirred")
except AttributeError as err:
    print(err)

