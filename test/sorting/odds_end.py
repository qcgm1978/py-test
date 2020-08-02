
import unittest
from operator import itemgetter
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
class TDD_ODDS_END(unittest.TestCase):
    def test_odds_end(self):
        data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
        standard_way = sorted(data, key=itemgetter(0), reverse=True)
        double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
        self.assertEqual( standard_way , double_reversed)
        self.assertEqual(standard_way, [('red', 1), ('red', 2), ('blue', 1), ('blue', 2)])
    def test_lt(self):
        Student.__lt__ = lambda self, other: self.age < other.age
        self.assertEqual(str(sorted(student_objects)),str([
            Student('dave', 'B', 10),
            Student('jane', 'B', 12),
            Student('john', 'A', 15),
        ]))
        students = ['dave', 'john', 'jane']
        newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
        s=sorted(students, key=newgrades.__getitem__)
        self.assertEqual(s,[ 'jane','dave', 'john',])
if __name__ == '__main__':
    unittest.main()

                