
import time
import logging

def virtual(old_func):
    '''
        decorator -- makes method raise NotImplementedError
    '''
    def new_func():
        raise NotImplementedError
    return new_func

def timestamp(old_func):
    def new_func(*args,**kwargs):
        tstamp = time.ctime()
        return (old_func(*args,**kwargs),tstamp)
    return new_func

def logtimestamp(old_func):
    logger = logging.getLogger('demo')
    hdlr = logging.FileHandler('demo.log')
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(hdlr)

    def new_func(*args,**kwargs):
        tstamp = time.ctime()
        logger.info(old_func.__name__)
        old_func(*args,**kwargs)
    return new_func

class logtimes():
    def __init__(self,filename):
        self._filename = filename

        self._logger = logging.getLogger('demo')
        hdlr = logging.FileHandler(self._filename)
        formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
        hdlr.setFormatter(formatter)
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(hdlr)
      
    def __call__( self, old_func ):
        def new_func(*args):
            self._logger.info('starting')
            old_func(*args)  # call the 'real' function
            self._logger.info('ending')
        return new_func

if __name__ == '__main__':

    @logtimes('barf.log')
    def foo(x,y):
        return x + y

    # x = timestamp(foo)

    @logtimes('barf.log')
    def bar():
        print("In bar")

    x1 = foo(1,2)
    x2 = foo(5,10)
    x3 = foo('a','b')
    print(x1)
    print(x2)
    print(x3)

        
    print(bar())
    print(bar())