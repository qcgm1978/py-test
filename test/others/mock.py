# Dot product of two arrays. Specifically,
import os
import unittest
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append("/Users/zhanghongliang/Documents/py-test")

class MockTest(unittest.TestCase):
        def assertEqualAll(*args):
            for i in range(len(args)-1):
                v=args[i+1]
                if v != args[1]:
                    wrong = str(v)
                    first = str(args[0])
                    ret=f"The {i+1}th arg {wrong} is not equal to the first arg {first}"
                    raise AssertionError(ret)

        unittest.TestCase.assertEqualAll = assertEqualAll

if __name__ == "__main__":
    unittest.main()

