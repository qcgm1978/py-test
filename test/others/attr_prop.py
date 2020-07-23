
# https: // stackoverflow.com / questions / 7374748 / whats - the - difference - between - a - python - property - and - attribute
import unittest
class TDDattr_prop(unittest.TestCase):
    def test_attr_prop(self):
        class SomeObject:
            # Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class. Therefore they have the same value for every instance. We define class attributes outside all the methods, usually they are placed at the top, right below the class header.
            eggs = "I am a class attribute!"
            '''A._x is an attribute'''
            _x = 0
            @property
            def x(self):
                '''
                A.x is a property
                This is the getter method
                '''
                return self._x

            @x.setter
            def x(self, value):
                """
                This is the setter method
                where I can check it's not assigned a value < 0
                """
                if value < 0:
                    raise ValueError("Must be >= 0")
                self._x = value
            def __get__(self,key):
                return 'current key is: ' + key
            def __init__(self, name, physic_health, mental_health):
                self.test = self.test_func()
                self.name=name
                self.__physic_health=physic_health #physic_health is real value in range [0, 5.0]
                self.__mental_health=mental_health #mental_health is real value in range [0, 5.0]
            @property
            def condition(self):
                health=self.__physic_health+self.__mental_health
                if(health<5.0):
                    return "I feel bad!"
                elif health<8.0:
                    return "I am ok!"
                else:
                    return "Great!" 
            def test_func(self):
                # print ('func running')
                return 'func value'
        spam = SomeObject('name', 10,3)
        self.assertEqual(spam.eggs, "I am a class attribute!")
        spam.eggs = 'eggs'
        self.assertEqual(spam.eggs, 'eggs')
        self.assertEqual(spam._x,0)
        self.assertEqual(spam.x, 0)
        spam._x = -1
        self.assertEqual(spam._x,-1)
        self.assertEqual(spam.x, -1)
        self.assertRaises(ValueError,lambda: setattr(spam,'x', -1) )
        self.assertEqual(spam.test, 'func value')
        self.assertRaises(AttributeError, lambda: spam.__physic_health)  #__physic_health and __mental_health are private and can not be accessed directly from out side, the only way outside class interact with them is throught property condition
        self.assertEqual(spam.name, 'name')
        self.assertEqual(spam.condition,"Great!")
if __name__ == '__main__':
    unittest.main()

                