import random
import unittest
class TDD_RANDOM(unittest.TestCase):
    def test_random(self):
        random.seed(10)
        r1 = random.random()
        self.assertLess(r1, 1)
        random.seed(10)
        r2 = random.random()
        self.assertEqual(r1, r2)
    def test_getstate(self):
        r = random.getstate()
        # print(r)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 3)
        self.assertEqual(r[0], 3)
        self.assertIsInstance(r[1], tuple)
        self.assertIsNone(r[2])
    def test_setstate(self):
        r1 = random.random()
        # capture the state:
        state = random.getstate()
        # print another random number:
        r2 = random.random()
        self.assertNotEqual(r1, r2)
        # restore the state:
        random.setstate(state)
        # and the next random number should be the same as when you captured the state:
        r3 = random.random()
        self.assertEqual(r2, r3)
    def test_getrandbits(self):
        e = random.getrandbits(8)
        binE = bin(e)
        # Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
        bitE = e.bit_length()
        # If x is zero, then x.bit_length() returns 0.
        self.assertEqual(len(binE[2:]), bitE if e else 0)
        self.assertLessEqual( bitE,8)
    def test_randrange(self):
        r = random.randrange(3, 9,6)
        self.assertIsInstance(r, int)
        self.assertLess(r,9)
        self.assertGreaterEqual(r,3)
    def test_randint(self):
        i = random.randint(3, 9)
        self.assertIsInstance(i, int)
        self.assertLessEqual(i,9)
        self.assertGreaterEqual(i,3)
        self.assertEqual(random.randrange(0,1),0)
        self.assertTrue(random.randint(0,1) in [0,1])
    def test_choice(self):
        mylist = ["apple", "banana", "cherry"]
        c = random.choice(mylist)
        self.assertTrue(c in mylist)
        x = "WELCOME"
        self.assertTrue(random.choice(x) in x)
    def test_choices(self):
        mylist = ["apple", "banana", "cherry"]

        c = (random.choices(mylist, weights=[10, 1, 1], k=14))
        # print(c)
        self.assertEqual(len(c), 14)
        # self.assertGreaterEqual(c.count('apple')-c.count('banana'),10)
    def test_shuffle(self):
        mylist= ["apple", "banana", "cherry"]
        mylist1= mylist.copy()
        s=random.shuffle(mylist)
        self.assertIsNone(s)
        self.assertCountEqual(mylist,mylist1)
        def myfunction():
          return 0.1

        mylist = ["apple", "banana", "cherry"]
        random.shuffle(mylist, myfunction)
        self.assertEqual(mylist,['banana', 'cherry', 'apple'])
    def test_sample(self):
        mylist = ["apple", "banana", "cherry"]

        self.assertCountEqual(random.sample(mylist, k=2),['banana', 'apple'])
        self.assertCountEqual(list(filter(lambda x: not x in 'mylist',random.sample('mylist', k=2))), [])
    def test_random_random(self):
        r=random.random()
        self.assertGreater(r, 0)
        self.assertLess(r,1)
    def test_uniform(self):
        random.seed(20)
        u = random.uniform(20, 60)
        self.assertGreaterEqual(u,20)
        self.assertLessEqual(u,60)
    def test_triangular(self):
        t = random.triangular(20, 60, 30)
        self.assertIsInstance(t,float)
        self.assertLessEqual(t,60)
        self.assertGreaterEqual(t,20)
if __name__ == "__main__":
    unittest.main()
