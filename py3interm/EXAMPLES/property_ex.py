#!/usr/bin/python3


class Foo(object):
    def __init__(self,f=1):
        self._f = f

    def get_f(self):
        print("getting F")
        return self._f

    def set_f(self,value):
        print("setting F to",value)
        self._f =  value

    def del_f(self):
        print("deleting F")
        del self._f

    F = property(get_f,set_f,del_f,"The F property")

class Bar(object):
    def __init__(self,b=1):
        self._b = b

    @property
    def B(self):
        print("getting B")
        return self._b

    @B.setter
    def B(self,value):
        print("setting B to",value)
        self._b =  value

    @B.deleter
    def B(self):
        print("deleting B")
        del self._b

if __name__ == '__main__':
    f1 = Foo()
    f1.F = 42
    print(f1.F)
    del f1.F

    print()

    b1 = Bar()
    b1.B = 'Zaphod'
    print(b1.B)
    del b1.B

