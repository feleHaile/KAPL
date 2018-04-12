#!/usr/bin/python3
from functools import wraps

def debugger( old_func ):

    @wraps(old_func)
    def new_func( *args, **kwargs ):
        print("*" * 40)
        print("** function", old_func.__name__,"**")

        if args:
            print("\targs are ", args)
        if kwargs:
            print("\tkwargs are ", kwargs)

        print("*" * 40)

        return old_func( *args, **kwargs )  # call the target function

    return new_func   # return the new function object


@debugger
def hello( greeting, whom ):
    print("{0}, {1}".format( greeting, whom ))
    
hello('hello','world')
hello('hi','Earth')
