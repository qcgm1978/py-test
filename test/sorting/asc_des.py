
import unittest,collections
from operator import itemgetter,attrgetter
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
class TDD_ASC_DES(unittest.TestCase):
    def test_asc_des(self):
        s = sorted(student_tuples, key=itemgetter(2), reverse=True)
        self.assertIsInstance(s,collections.Iterable)
        self.assertEqual(s,[
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
])
        s1=sorted(student_objects, key=attrgetter('age'), reverse=True)
        self.assertEqual(str(s1),str([
            Student('john', 'A', 15),
            Student('jane', 'B', 12),
            Student('dave', 'B', 10),
        ]))
    def test_stability_complex(self):
        data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
        s=sorted(data, key=itemgetter(0))
        self.assertEqual(s, [('blue', 1), ('blue', 2), ('red', 1), ('red', 2),])
        s1 = sorted(student_objects, key=attrgetter('age'))  # sort on secondary key
        self.assertEqual(str(s1),str([
            Student('dave', 'B', 10),
            Student('jane', 'B', 12),
            Student('john', 'A', 15),
        ]))
        s2 = sorted(s1, key=attrgetter('grade'), reverse=True)
        self.assertEqual(str(s2),str([
            Student('dave', 'B', 10),
            Student('jane', 'B', 12),
            Student('john', 'A', 15),
        ]))
        def multisort(xs, specs):
            for key, reverse in reversed(specs):
                xs.sort(key=attrgetter(key), reverse=reverse)
            return xs
        s3 = multisort(list(student_objects), (('grade', True), ('age', False)))
        self.assertEqual(str(s3),str(s2))

if __name__ == '__main__':
    unittest.main()

                