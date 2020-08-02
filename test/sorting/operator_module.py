from operator import itemgetter, attrgetter
import unittest
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
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
class TDD_OPERATOR_MODULE(unittest.TestCase):
    def test_operator_module(self):
        s=sorted(student_tuples, key=itemgetter(2))
        s1=sorted(student_tuples, key=lambda student:student[2])
        self.assertEqual(s,[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)])
        self.assertEqual(s1, [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)])
        
        
        s=sorted(student_objects, key=attrgetter('age'))
        s1=sorted(student_objects, key=lambda student: student.age)   # sort by age
        self.assertEqual(str(s),str([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]))
        self.assertEqual(str(s1), str([('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]))
    def test_multi_levels(self):
        s=sorted(student_tuples, key=itemgetter(1,2))
        self.assertEqual(s,[
    ('john', 'A', 15),
    ('dave', 'B', 10),
    ('jane', 'B', 12),
])
        s1=sorted(student_objects, key=attrgetter('grade', 'age'))
        self.assertEqual(s,[
    ('john', 'A', 15),
    ('dave', 'B', 10),
    ('jane', 'B', 12),
])

if __name__ == '__main__':
    unittest.main()

                