
import unittest,re
class TDD_MATCH_SEARCH(unittest.TestCase):
    def test_match_search(self):
        self.assertEqual(re.match('super', 'superstition').span(),(0, 5))
        
        self.assertIsNone(re.match('super', 'insuperable'))
    def test_seach_scan_forward(self):
        self.assertEqual(re.search('super', 'superstition').span(),(0, 5))
        self.assertEqual(re.search('super', 'insuperable').span(),(2,7))
if __name__ == '__main__':
    unittest.main()

                