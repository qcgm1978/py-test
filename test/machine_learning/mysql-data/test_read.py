import unittest
from mysqlOp import MysqlOp
class TDD_READ(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('customers')
        return super().setUp()
    def test_table(self):
        self.m.showTables()
        self.assertIsInstance(self.m.mycursor, object)
        for k in self.m.mycursor:
            self.assertTrue(k in [('customers',),('users',),('products',)])
    def test_select(self):
        s = self.m.select()
        self.assertEqual(len(s),self.m.mycursor.rowcount)
        s1 = self.m.select(limit=1)
        s2 = self.m.select(limit=2,offset=12)
        self.assertEqual(len(s1),1)
        self.assertEqual(len(s2),2)
        self.assertEqual(len(s),self.m.getRowsCount())
        first=('John', 'Highway 21')
        self.assertEqual(s[0][:2],first)
        s1 = self.m.selectColumns(['name', 'address'])
        self.assertEqual(s1[0],('John', 'Highway 21'))
        self.assertEqual(self.m.fetchOne()[:2], first)
    def test_filter(self):
        f=self.m.where({'address' :'Park Lane 38'})
        f1=self.m.where({'address' :'Park Lane 38'})
        self.assertEqual(f[0][:2],('Ben', 'Park Lane 38'))
    def test_wild(self):
        w=self.m.wild({'address':'way'})
        w=map(lambda item:item[:2],w)
        self.assertEqual(list(w),[('John', 'Highway 21'), ('Susan', 'One way 98'), ('Viola', 'Sideway 1633')])
    def test_escape(self):
        adr = ("Yellow Garden 2", )
        e=self.m.escape(adr)
        self.assertEqual(e[0][:2],('Vicky', 'Yellow Garden 2'))
    def test_sort(self):
        s=self.m.sort('name')
        s1=self.m.sort('name',True)
        self.assertEqual(s[0][0],'Amy')
        self.assertEqual(s[-1][0],'William')
        self.assertEqual(s1[-1][0],'Amy')
        self.assertEqual(s1[-1][0],s[0][0])
        self.assertEqual(s1[0][0],s[-1][0])
if __name__ == '__main__':
    unittest.main()
