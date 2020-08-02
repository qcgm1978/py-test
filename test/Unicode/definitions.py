
import unittest
class TDD_DEFINITIONS(unittest.TestCase):
    def test_definitions(self):
        self.assertEqual("\u0061",'a');# LATIN SMALL LETTER A
        self.assertEqual('\u0062','b') #  LATIN SMALL LETTER B
        self.assertEqual('\u0063','c') #  LATIN SMALL LETTER C
        self.assertEqual('\u007B','{') #  LEFT CURLY BRACKET
        self.assertEqual('\u2167','Ⅷ') #  ROMAN NUMERAL EIGHT
        self.assertEqual('\u2168','Ⅸ') #  ROMAN NUMERAL NINE
        self.assertEqual('\u265E','♞') #  BLACK CHESS KNIGHT
        self.assertEqual('\u265F','♟') #  BLACK CHESS PAWN
        self.assertEqual(u"\U0001F600",'😀') #  GRINNING FACE
        self.assertEqual(u'\U0001F609','😉') #  WINKING FACE
if __name__ == '__main__':
    unittest.main()

                