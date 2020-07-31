
import unittest
class TDD_KEY_FUNCTIONS(unittest.TestCase):
    def test_key_functions(self):
        s=sorted("This is a test string from Andrew".split(), key=str.lower)
        s1=sorted("This is a test string from Andrew".split())
        self.assertEqual(s,['a', 'Andrew', 'from', 'is', 'string', 'test', 'This'])
        self.assertEqual(s1, ['Andrew', 'This', 'a', 'from', 'is', 'string', 'test'])
        student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
        s2=sorted(student_tuples, key=lambda student: ~student[2])   # sort by age
        self.assertEqual(s2, list(reversed([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)])))
    def test_named_attributes(self):
        class Student:
            def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
            def __repr__(self):
                return repr((self.name, self.grade, self.age))
        student_objects = [
            Student('john', 'A', 15),
            Student('jane', 'B', 12),
            Student('dave', 'B', 10),
        ]
        s=sorted(student_objects, key=lambda student: student.age)   # sort by age
        self.assertEqual(str(s),str([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]))
if __name__ == '__main__':
    unittest.main()

                