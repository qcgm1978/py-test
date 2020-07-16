import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from utilities.getArr import getArr
def isAny(a,*args,**kwargs):
    axis=0
    for key, value in kwargs.items(): 
        axis=value 
    if args:
        b=args[0]
        return a==b
    else:
        b=a[1]
        a=a[0]
        aList=getArr(len(a),len(b))
        for i in range(len(a)) :
            if(a[i]==b[i]):
                return 1
        return 0