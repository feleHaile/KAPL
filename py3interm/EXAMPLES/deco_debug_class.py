#!/usr/bin/python3

class debugger(object):
    def __init__(self,func):
        self._func = func

    def __call__( self, *args, **kwargs ):
        print("*" * 40)
        print("** function", self._func.__name__,"**")

        if args:
          print("\targs are ", args)
        if kwargs:
          print("\tkwargs are ", kwargs)

        print("*" * 40)

        return self._func( *args, **kwargs )  # call the 'real' function

@debugger
def hello( greeting, whom ):
    print("{0}, {1}".format( greeting, whom ))
    
hello('hello','world')
hello('hi','Earth')
