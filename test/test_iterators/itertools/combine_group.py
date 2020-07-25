import unittest
import os, itertools, collections


class test_combinations(unittest.TestCase):
    def test_possible_tuple(self):
        i=itertools.combinations([1, 2, 3, 4, 5], 2)
        self.assertIsInstance(i,collections.Iterable)
        self.assertEqual(tuple(i),((1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5)))
        i2 = itertools.combinations([1, 2, 3, 4, 5], 3)
        self.assertEqual(list(i2),[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5),
(3, 4, 5)])
        i3 = itertools.permutations('aba', 3)
        self.assertEqual(list(i3),[('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'), ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')])
        i4 = itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2)
        self.assertEqual(list(i4),[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 2), (2, 3), (2, 4), (2, 5),
(3, 3), (3, 4), (3, 5),
  (4, 4), (4, 5),
  (5, 5)])
    def test_group(self):
        city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'), ('Anchorage', 'AK'), ('Nome', 'AK'),('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')]
        def get_state(city_state):
            return city_state[1]
        i1=itertools.groupby(city_list, get_state)
        # self.assertEqual(list(i1)[0][0],'AL')
        self.assertIsInstance(list(i1)[0][1],itertools._grouper)
if __name__ == "__main__":
    unittest.main()
