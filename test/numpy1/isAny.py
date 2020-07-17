import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from utilities.getArr import getArr
import numpy as np
import math
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
def isAny(a,*args,**kwargs):
    try:
        if math.isnan(float(a)):
            return 1
    except:
        pass
    axis=1
    out=None
    for key, value in kwargs.items(): 
        if(key=='axis'):
            axis=value
        if(key=='out'):
            out=value

    if args:
        b=args[0]
        return a==b
    else:
        if type(max(a))==list:
            b=a[1]
            a=a[0]
            aList=getArr(len(a),len(b))
            end=range(len(a))
            for i in end :
                if axis:
                    eql=a[i]==b[i]
                    if(eql):
                        if out:
                            out=1
                        else:
                            return 1
                else:
                    aList[i]=a[i] or b[i]
        else:
            end=range(len(a))
            for i in end :
                if axis:
                    eql=a[i]
                    if(eql):
                        if out:
                            globals()[out]=1
                            return 1
                        else:
                            return 1
                else:
                    aList[i]=a[i] or b[i]
        
        if axis:
            if out:
                out=0
            else:
                return 0
        else:
            return np.array(aList)