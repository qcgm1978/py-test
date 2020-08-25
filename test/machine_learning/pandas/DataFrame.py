# pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
import unittest, pandas as pd
import numpy as np
class TDD_DATAFRAME(unittest.TestCase):
    def setUp(self):
        data = {'name': ['Jack', 'Frank', 'Kelly', 'Rebecca', "Monica"], 
        'year': [2015, 2011, 2010, 2014, ''], 
        'reports': [24, 4, 2, 31, None]}
        self.df = pd.DataFrame(data, index = ['New York', 'New Orleans', 'Budapest', 'Helsinki', "Cologne"])
        return super().setUp()
    # pandas.DataFrame.loc
    # property DataFrame.loc
    # Access a group of rows and columns by label(s) or a boolean array.
    def test_DataFrame_loc(self):
        df = pd.DataFrame(
            [[1, 2], [4, 5], [5, 8]],
            index=['cobra', 'viper', 'sidewinder'],
            columns=['max_speed', 'shield']
        )
        self.assertEqual(df.shape, (3, 2))
        l=df.loc[df['shield'] > 6]
        self.assertEqual(list(l.values[0]), [5, 8])
        l=df.loc[df['shield'] > 6, ['max_speed']]
        self.assertEqual(list(l.values[0]), [5])
        l=df[(df['shield'] > 6) & (df['max_speed']>6)]
        self.assertEqual(list(l.values), [])
        l=df[(df['shield'] > 6) & (df['max_speed']<6)]
        self.assertEqual(list(l.values[0]), [5,8])
        # http://scrapingauthority.com/pandas-dataframe-filtering/
        # 7 Ways To Filter A Pandas Dataframe
    def test_get_columns(self):
        n=self.df['name']
        self.assertEqual(list(n), ['Jack', 'Frank', 'Kelly', 'Rebecca', "Monica"])
        n = self.df[['name', 'year']]
        print(n.values)
        self.assertEqual(n.values.tolist(), [
            ['Jack', 2015.0],
            ['Frank' ,2011.0],
            ['Kelly' ,2010.0],
            ['Rebecca', 2014.0],
            ['Monica', '']
        ])
if __name__ == '__main__':
    unittest.main()
