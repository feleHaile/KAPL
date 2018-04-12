#!/usr/bin/env python
# (c) 2016 John Strickler
#

class FileFilter():
    FUNCTIONS = []

    def __init__(self, file_name):
        self._file = None
        self._file_name = file_name
        self._file = open(self._file_name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._file.close()

    @classmethod
    def register(cls, func):
        '''
        Decorator for registering line filters
        '''
        cls.FUNCTIONS.append(func)
    
        # no need to modify function
        return func

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._file)
        for filter in self.FUNCTIONS:
            line = filter(line)
        return line

