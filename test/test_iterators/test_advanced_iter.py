import unittest,re


class TDDDiveIntoPython3(unittest.TestCase):
    def test_class(self):
        a_list=re.findall('[0-9]+','16 2-by-4s in rows of 8')
        self.assertEqual(a_list,['16','2','4','8'])
        a_list=re.findall('[A-Z]+','SEND + MORE == MONEY')
        self.assertEqual(a_list,['SEND','MORE', 'MONEY'])
        a_list= re.findall(' s.* s', "The sixth sick sheikh's sixth sheep's sick.")
        self.assertEqual(a_list,[' sixth sick sheikh\'s sixth sheep\'s s'])
        a_list= re.findall(' s.*? s', "The sixth s','sheikh's s','sheep's s")
    def test_find_unique(self):
        a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
        self.assertEqual(set(a_list),{'The', 'sixth', 'sick', "sheik's", "sheep's"})
        a_string = 'EAST IS EAST'
        self.assertEqual(set(a_string),{'E','A','S','T',' ','I'})
        words = ['SEND', 'MORE', 'MONEY']
        a_string = ''.join(words)
        self.assertEqual(a_string,'SENDMOREMONEY')
        self.assertEqual(set(a_string),{'S','E','N','D','M','O','R','Y'})

    def test_assert(self):
        def assert_error(str):
            unique_characters=set(str)
            if len(unique_characters)>10:
                raise AssertionError('Too many letters')
        try:
            assert 1+1==2
            assert 1+2==3
            assert_error('abc')
            assert_error('abcdefghij')
            assert_error('abcdefghijj')
        except AssertionError:
            self.fail('AssertionError Raised')

    def test_gen_expression(self):
        unique_characters=['E','D','M','O','N','S','R','Y']
        gen=(ord(c) for c in unique_characters)
        self.assertIsInstance(gen,object)
        self.assertEqual(next(gen),69)
        self.assertEqual(next(gen),68)
        a_tuple=tuple(gen)
        self.assertEqual(len(a_tuple),6)
        self.assertEqual(a_tuple,(77,79,78,83,82,89))

if __name__ == '__main__':
    unittest.main()