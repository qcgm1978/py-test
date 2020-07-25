import os, unittest
class TestPath(unittest.TestCase):
    def test_join(self):
# Join one or more path components intelligently.
        p=os.path.join("c:", "foo")
        self.assertEqual(p,'c:/foo')
unittest.main()
