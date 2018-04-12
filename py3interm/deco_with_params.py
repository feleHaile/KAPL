#!/usr/bin/env python

def outer(color):

    def inner(old_func):

        def wrapper(*args, **kwargs):
            print("color is", color)
            return old_func(*args, **kwargs)

        return wrapper

    return inner

@outer('blue')
def spam():
    print("IN SPAM")

@outer('orange')
def ham():
    print("IN HAM")

# ham = outer('orange')(ham)

spam()
ham()

# @foo
# def bar():
#     pass

#  bar = foo(bar)
