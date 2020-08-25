# pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
import unittest,pandas
class TDD_DATAFRAME(unittest.TestCase):
    # pandas.DataFrame.loc
    # property DataFrame.loc
    # Access a group of rows and columns by label(s) or a boolean array.
    def test_DataFrame_loc(self):
        df = pandas.DataFrame(
            [[1, 2], [4, 5], [5, 8]],
            index=['cobra', 'viper', 'sidewinder'],
            columns=['max_speed', 'shield']
        )
        self.assertEqual(df.shape, (3, 2))
        l=df.loc[df['shield'] > 6]
        self.assertListEqual(list(l.values[0]),[5,8])
if __name__ == '__main__':
    unittest.main()
