
import unittest
class TDDmap(unittest.TestCase):
    def test_map(self):
        # Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().
        import collections
        def square(x) :            # 计算平方数
            return x ** 2
        
        s=map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
        self.assertIsInstance(s, collections.Iterable)
        l=[]
        for ele in s:
            l.append(ele)
        self.assertEqual(l, [1, 4, 9, 16, 25])
        l1=[]
        s1 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
        for ele in s1:
            l1.append(ele)
        self.assertEqual(l1, [1, 4, 9, 16, 25])
    
    # 提供了两个列表，对相同位置的列表数据进行相加
        it=map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
        l2=[]
        for ele in it:
            l2.append(ele)
        self.assertEqual(l2,[3,7,11,15,19])
if __name__ == '__main__':
    unittest.main()

                