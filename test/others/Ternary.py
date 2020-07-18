import unittest


class TestIs(unittest.TestCase):
    def testArgs(self):
        is_nice = True
        state = "nice" if is_nice else "not nice"
        self.assertEqual(state, 'nice')
    def testTuple(self):
        bool = True
        personality = ("mean", "nice")[bool]
        self.assertEqual("The cat is " + personality, 'The cat is nice')
        condition = True
        self.assertEqual(2 if condition else 1/0,2)
        self.assertRaises(ZeroDivisionError, lambda:(1/0, 2)[condition])
    def testShorthand(self):
        self.assertTrue(True or "Some")
        self.assertEqual(False or "Some",'Some')
        output = None
        self.assertEqual(output or "No data returned", 'No data returned')
        def my_function(real_name, optional_display_name=None):
            optional_display_name = optional_display_name or real_name
            return (optional_display_name)
            self.assertEqual(my_function("John"),'John')
            self.assertEqual(my_function("Mike", "anonymous123"),'anonymous123')
if __name__ == "__main__":
    unittest.main()
