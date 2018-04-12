#!/usr/bin/env python
import sys
import sh

if sys.platform == 'win32':
    print("Sorry, the sh module is only implemented on non-Windows systems")
    exit(1)

print(sh.ls('-l','../DATA/parrot.txt'))
print('-' * 50)

from sh import ls
print(ls('-l', '../DATA/parrot.txt'))
print('-' * 50)

ll = ls.bake(l=True)
print(ll('../DATA'))
print('-' * 50)

from sh import ls, glob
print(ls('-ld', glob('/etc/pr*')))
print('-' * 50)

w = sh.who()
print(w)
print('-' * 50)

disk_usage = sh.df('-h')
print(disk_usage)
print('-' * 50)

from sh import uname
print(uname())
print(uname('-a'))
print(uname(a=True))
print('-' * 50)

from sh import grep, wc

# grep 'sh' /etc/passwd | wc -l
print(grep('sh', '/etc/passwd'))
print(wc(grep('sh', '/etc/passwd'), l=True))
print('-' * 50)

from sh import tr
fruits = 'apple banana mango orange'.split()
print(tr("[:lower:]", "[:upper:]", _in=fruits))
