import unittest
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.calculator import Calculator  # pylint: disable=import-error
from app.humansize import approximate_size  # pylint: disable=import-error


class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_path(self):
        self.assertNotEqual(sys.path, list)

    def test_human(self):
        self.assertEqual(approximate_size(4096, True), '4.0 KiB')
        self.assertIsInstance(approximate_size.__doc__, str)

    def test_human(self):
        self.assertRaises(ValueError, approximate_size, -1, True)

    def test_bool_num(self):
        self.assertEqual(1, True)
        self.assertEqual(True+True, 2)
        self.assertEqual(True-False, 1)
        self.assertEqual(True*False, 0)

        def falseAsZero():
            True/False
        self.assertRaises(ZeroDivisionError, falseAsZero)
        self.assertIsInstance(1, int)
        self.assertTrue(isinstance(1, int))
        self.assertEqual(1+1.0, 2.0)
        self.assertEqual(type(1+1.0), float)
        self.assertTrue(isinstance(1+1.0, float))
        self.assertIsInstance(2.0, float)
        self.assertIsInstance(float(2), float)
        self.assertIsInstance(int(2.1), int)
        self.assertEqual(int(2.1),2)
        self.assertEqual(int(2.7),2)


if __name__ == '__main__':
    unittest.main()
