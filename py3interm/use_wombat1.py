#!/usr/bin/env python
import os
import sys

import hedgehog
from kapl.misc import wombat

hedgehog.print_food()

wombat.FOOD.append('doughnuts')

wombat.shuffle()
print(wombat.FOOD[0])

# print(wombat.re.IGNORECASE)   PHEW! CODE SMELL

#  ., PYTHONPATH, PREFIX/...
print(os.path.join(sys.prefix, 'lib'))

print()
for path in sys.path:
    print(path)
print()

print(sys.version_info)
print(sys.executable)
