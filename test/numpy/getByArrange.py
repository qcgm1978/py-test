import numpy as np


def getByArrange(start=0,*args):
    interval=1
    if args:
        if len(args)>1:
           interval=args[1]
        end = args[0]
    else:
        end = start
        start=0
    aList = []
    end = int(round(end))
    aList=list(range(start,end,interval))
    return np.array(aList)
    # a = np.arange(3)
    # self.assertFalse((a - [0, 1, 2]).any())
    # self.assertFalse((np.arange(3.0) - [0.0, 1.0, 2.0]).any())
    # self.assertFalse((np.arange(3, 7) - [3, 4, 5, 6]).any())
    # self.assertFalse((np.arange(3, 7, 2) - [3, 5]).any())
