#!/usr/bin/env python3

def main():
    ss = SillyString('this is a test')

    print(ss.every_other())
    print()

    ss2 = SillyString('Dximd8 *i@tz !w7ogrvkb?#')

    print(ss2.every_other())

def _every_other(self):
    return self._string[::2]

def _init(self, string):
    self._string = string

SillyString = type(
    'SillyString',
    (object,),
    {'__init__': _init, 'every_other': _every_other}
)

if __name__ == '__main__':
    main()
