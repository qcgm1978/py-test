# Dot product of two arrays. Specifically
import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from utilities.getArr import getArr
def isComplexNum(i):
    num = i[0] if isinstance(i, list) else i
    return isinstance(num, complex)


def dotTwo(a, b):
    isComplex = isComplexNum(a)
    a = getList(a)
    b = getList(b)
    if hasattr(a,'__len__'):
        total = 0
        if isComplex:
            for i in range(len(a)):
                total -= a[i] * b[i]
        else:
            total, cols = getMat(a, b)
            for i in range(len(a)):
                lenM = len(a[i])
                for m in range(lenM):
                    tot = ind = 0
                    for n in range(cols):
                        tot += a[i][n] * b[m][n]
                    total[m][i] = tot
    else:
        total = a * b
    return total


def getMat(a, b):
    row = len(a)
    cols = len(b[0])
    total = getArr(row, cols)
    return total, cols




def getList(arr):
    if type(arr) == list:
        a_list = []
        for i in arr:
            if isComplexNum(i):
                m = int(i.imag)
            else:
                m = i
            a_list.append(m)
    else:
        a_list = arr
    return a_list
