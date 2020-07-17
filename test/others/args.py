import unittest


class TestIs(unittest.TestCase):
    def testArgs(self):
        # Python program to illustrate 
        # *args for variable number of arguments 
        def myFun(*argv): 
            aList=[]
            for arg in argv: 
                aList.append (arg) 
            return aList
        self.assertListEqual(myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') ,['Hello', 'Welcome', 'to', 'GeeksforGeeks'])
    def testFirstArg(self):
        def myFun(arg1, *argv): 
            aList=[]
            aList.append( arg1) 
            for arg in argv: 
                aList.append( arg) 
            return aList
        bList=myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
        self.assertEqual(bList, ['Hello', 'Welcome', 'to', 'GeeksforGeeks'])
    def testKeywordArgs(self):
        # *kargs for variable number of keyword arguments 
        def myFun(**kwargs):
            alist=[] 
            for key, value in kwargs.items(): 
                alist.append ("%s = %s" %(key, value)) 
            return alist
        # Driver code 
        self.assertItemsEqual(myFun(first = 'Geeks', mid = 'for', last = 'Geeks'),['first = Geeks', 'mid = for', 'last = Geeks'])
    def testMixedKeywords(self):
        # variable number of keyword arguments with 
        # one extra argument. 
        
        def myFun(arg1, **kwargs):
            alist = []
            alist.append(arg1)
            for key, value in kwargs.items(): 
                alist.append ("%s = %s" %(key, value)) 
            return alist
        # Driver code 
        blist=myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 
        self.assertItemsEqual(blist,["Hi",'first = Geeks', 'mid = for', 'last = Geeks'])
    def testCallByStar(self):
        def myFun(arg1, arg2, arg3): 
            return (arg1,arg2,arg3)
            
        # Now we can use *args or **kwargs to 
        # pass arguments to this function :  
        args = ("Geeks", "for", "Geeks") 
        
        self.assertEqual(myFun(*args) ,args)
        kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
        self.assertEqual(myFun(**kwargs) ,("Geeks", "for", "Geeks"))
    def testMixed(self):
        def myFun(*args, **kwargs):
            alist=[]
            alist.append("args: "+ str(args) )
            alist.append("kwargs: "+str( kwargs) )
            return alist
        
        # Now we can use both *args ,**kwargs to pass arguments to this function : 
        self.assertEqual(myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") ,["args: ('geeks', 'for', 'geeks')","kwargs: {'last': 'Geeks', 'mid': 'for', 'first': 'Geeks'}"])
if __name__ == "__main__":
    unittest.main()
