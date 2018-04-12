#!/usr/bin/python3

from Debug import debug

class FruitError(Exception):
    """Picked a non-existent fruit"""
    def __init__(self):
        self.message = "You have selected an unapproved fruit"

approved_fruits = ['apple','orange','banana','elderberry','kiwi','guava','cherry']

fruit_registry = []

@debug
def registerFruit(fruit):
    if fruit in approved_fruits:
        fruit_registry.append(fruit)
    else:
        raise FruitError

for fruit in ['apple','lemon','kiwi']:
    try:
        registerFruit(fruit)
    except FruitError as f:
        print("Uh-oh,",f.message)

print("Registered fruits:", end=' ')
for fruit in fruit_registry:
    print(fruit, end=' ')
