import unittest
from maxArea import Solution
from intToRoman import Solution as Solution1
from romanToInt import Solution as Solution2
from longestCommonPrefix import Solution as Solution3
from threeSum import Solution as Solution4
from threeSumClosest import Solution as Solution5
from letterCombinations import Solution as Solution6
from fourSum import Solution as Solution7
class TDD_TEST11(unittest.TestCase):
    def test_test11(self):
        ins = Solution()
        n=ins.maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(n, 49)
    def test_intToRoman(self):
        ins = Solution1()
        s = ins.intToRoman(3)
        s1 = ins.intToRoman(4)
        s2 = ins.intToRoman(9)
        s3 = ins.intToRoman(58)
        s4 = ins.intToRoman(1994)
        s5 = ins.intToRoman(1)
        s6 = ins.intToRoman(2)
        s7 = ins.intToRoman(5)
        s8 = ins.intToRoman(6)
        s9 = ins.intToRoman(7)
        s10 = ins.intToRoman(10)
        s11 = ins.intToRoman(11)
        s12 = ins.intToRoman(12)
        s13 = ins.intToRoman(13)
        s14 = ins.intToRoman(14)
        s15 = ins.intToRoman(17)
        s16 = ins.intToRoman(21)
        s17 = ins.intToRoman(20)
        s18 = ins.intToRoman(40)
        s19 = ins.intToRoman(41)
        s20 = ins.intToRoman(50)
        s21 = ins.intToRoman(90)
        s22 = ins.intToRoman(100)
        s23 = ins.intToRoman(400)
        s24 = ins.intToRoman(500)
        self.assertEqual(s,"III")
        self.assertEqual(s1,"IV")
        self.assertEqual(s2,"IX")
        self.assertEqual(s3,"LVIII")
        self.assertEqual(s4,"MCMXCIV")
        self.assertEqual(s5,"I")
        self.assertEqual(s6,"II")
        self.assertEqual(s7,"V")
        self.assertEqual(s8,"VI")
        self.assertEqual(s9,"VII")
        self.assertEqual(s10,"X")
        self.assertEqual(s11,"XI")
        self.assertEqual(s12,"XII")
        self.assertEqual(s13,"XIII")
        self.assertEqual(s14,"XIV")
        self.assertEqual(s15,"XVII")
        self.assertEqual(s16,"XXI")
        self.assertEqual(s17,"XX")
        self.assertEqual(s18,"XL")
        self.assertEqual(s19,"XLI")
        self.assertEqual(s21,"XC")
        self.assertEqual(s22,"C")
        self.assertEqual(s23,"CD")
        self.assertEqual(s24,"D")
        self.assertEqual(ins.intToRoman(801),"DCCCI")
        self.assertEqual(ins.intToRoman(900),"CM")
        self.assertEqual(ins.intToRoman(1000),"M")
        self.assertEqual(ins.intToRoman(2000),"MM")
    def test_romanToInt(self):
        ins = Solution2()
        i=ins.romanToInt("III")
        self.assertEqual(i,3)
        self.assertEqual(ins.romanToInt('IV'),4)
        self.assertEqual(ins.romanToInt('IX'),9)
        self.assertEqual(ins.romanToInt('LVIII'),58)
        self.assertEqual(ins.romanToInt('MCMXCIV'),1994)
        self.assertEqual(ins.romanToInt('MCDLXXVI'),1476)
    def test_longestCommonPrefix(self):
        ins = Solution3()
        s=ins.longestCommonPrefix(["flower","flow","flight"])
        self.assertEqual(s,'fl')
        self.assertEqual(ins.longestCommonPrefix(["dog","racecar","car"]),'')
        self.assertEqual(ins.longestCommonPrefix([]),'')
        self.assertEqual(ins.longestCommonPrefix([""]),'')
    def test_threeSum(self):
        ins=Solution4()
        self.assertEqual(ins.threeSum([-1, 0, 1, 2, -1, -4]),[
            [-1, -1, 2],
            [-1, 0, 1],
        ])
        self.assertEqual(ins.threeSum([0,0,0]),[
            [0,0,0]
        ])
        self.assertEqual(ins.threeSum([-2,0,1,1,2]),[
            [2,0,-2],[-2,1,1]
        ])
        self.assertEqual(ins.threeSum([-2,0,0,2,2]),[
            [2,0,-2]
        ])
        self.assertEqual(len(ins.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])),len([
           [-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]
        ]))
        self.assertEqual((ins.threeSum([1, 4, -4, -5, -1, -2, -3, -4])), ([
            [-3, -1, 4],
            [-5, 1, 4],
            ]))
    def test_threeSumClosest(self):
        ins = Solution5()
        self.assertEqual(ins.threeSumClosest(nums = [-1,2,1,-4], target = 1),2)
        self.assertEqual(ins.threeSumClosest([1,1,1,1],-100),3)
    def test_letterCombinations(self):
        ins = Solution6()
        self.assertEqual(ins.letterCombinations("23"),["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(ins.letterCombinations("2"),["a","b","c"])
        self.assertEqual(ins.letterCombinations("7"),["p","q","r","s"])
        self.assertEqual(ins.letterCombinations("8"),['t', 'u', 'v'])
        self.assertEqual(ins.letterCombinations("9"), ['w', 'x', 'y', 'z'])
        self.maxDiff=None
        p = ins.letterCombinations("234")
        self.assertCountEqual(p,["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])
        self.assertEqual(ins.letterCombinations(""),None)
    def test_fourSum(self):
        ins = Solution7()
        l=ins.fourSum([1, 0, -1, 0, -2, 2],0)
        self.assertEqual(l,[
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
        ])
if __name__ == '__main__':
    unittest.main()

                