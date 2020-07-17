import unittest
import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from utilities.getArr import getArr
class TestIterate(unittest.TestCase):
    def setUp(self):
        self.list=[1, 3, 5, 7, 9] 
        self.aList=[0 for x in range(len(self.list))]
    def testLoop(self):
        # Using for loop 
        m=0
        for i in self.list: 
            self.aList[m] =i
            m+=1
        self.assertEqual(self.aList,self.list)
    def testRange(self):
        # getting length of list 
        length = len(self.list) 
        
        # Iterating the index 
        # same as 'for i in range(len(list))' 
        for i in range(length): 
            self.aList[i]=(self.list[i]) 
        self.assertEqual(self.aList,self.list)
    def testWhileLoop(self):
        # Getting length of list 
        length = len(self.list) 
        i = 0
   
        # Iterating using while loop 
        while i < length: 
            self.aList[i]=self.list[i]
            i += 1
        self.assertEqual(self.aList,self.list)
    def testComprehension(self):
        # Using list comprehension 
        self.aList=[(i) for i in self.list] 
        self.assertEqual(self.aList,self.list)
    def testEnumerate(self):
        for i, val in enumerate(self.list): 
             self.aList [i]=val
        self.assertEqual(self.aList,self.list)
    def testNumpy(self):
        import numpy as geek 
   
        # creating an array using   
        # arrange method 
        a = geek.arange(9) 
        self.assertEqual((a-[x for x in range(9)]).any(),0)
        # shape array with 3 rows   
        # and 4 columns 
        a = a.reshape(3, 3) 
        self.assertEqual(type(a),geek.ndarray)
        # self.assertListEqual(a,[[0,1,2],[3,4,5],[6,7,8]])
        # iterating an array 
        m=n=0
        aList=getArr(3,3)
        for x in geek.nditer(a): 
            aList[m][n]=x
            n+=1
            if n==3:
                m+=1
                n=0
        self.assertListEqual(aList,a.tolist())
if __name__ == "__main__":
    unittest.main()