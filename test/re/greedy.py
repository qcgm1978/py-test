import unittest, re


class TDD_GREEDY(unittest.TestCase):
    def test_greedy(self):
        s = "<html><head><title>Title</title>"
        length = len(s)
        self.assertEqual(length, 32)
        self.assertEqual(re.match("<.*>", s).span(), (0, length))
        self.assertEqual(re.match("<.*>", s).group(), s)
        self.assertEqual(re.match("<.*?>", s).group(), s.split(">")[0] + ">")
        p = re.compile(r"(>)")
        splitS = p.split(s)
        self.assertEqual(re.match("<.*?>", s).group(), splitS[0] + splitS[1])
    def test_verbose(self):
        pat = re.compile(r"""
\s*# Skip leading whitespace

 (?P<header>[^:]+)# Header name
  \s* :# Whitespace, and a colon

 (?P<value># The header's value --
 .*?)#  *? used to
# lose the following trailing whitespace
\s*$ # Trailing whitespace to end-of-line
""" , re.VERBOSE)
        pat1 = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")

if __name__ == "__main__":
    unittest.main()

