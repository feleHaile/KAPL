#!/usr/bin/python3

class Rabbit:
    weapon = 'pointy teeth'

    def get_weapon(self):
        print("INSTANCE: ({0}) {1}".format(self,Rabbit.weapon))

    @classmethod
    def get_weapon_again(cls):
        print("CLASS: ({0}) {1}".format(cls,cls.weapon))

r = Rabbit()

r.get_weapon()
r.get_weapon_again()
Rabbit.get_weapon_again()
print(Rabbit.weapon)