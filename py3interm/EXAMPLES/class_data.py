#!/usr/bin/python3

import sys

#!/usr/bin/python3

class Rabbit:
    weapon = 'a nice cup of tea'
    name = 'Roger'
    
    def __init__(self):
        self.weapon = 'pointy teeth'
        
    def display(self):
        print("weapon -- CLASS: {0} INSTANCE: {1}".format(Rabbit.weapon,self.weapon))
        print("name -- CLASS: {0} INSTANCE: {1}".format(Rabbit.name,self.name))
        

r = Rabbit()
r.display()
