#!/usr/bin/env python

class HTMLWrapper():

    def __init__(self, tag):
        self._tag = tag

    def __call__(self, text):
        return '<{0}>{1}</{0}>'.format(self._tag, text)

if __name__ == '__main__':
    h1 = HTMLWrapper('h1')
    print(h1('spam'))  # h1.__call__('spam')
    div = HTMLWrapper('div')
    print(div('ham'))
