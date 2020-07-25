import unittest


class TDDproperties(unittest.TestCase):
    def test_properties(self):
        class C(object):
            def getx(self):
                return self.__x

            def setx(self, value):
                self.__x = value

            def delx(self):
                del self.__x

            x = property(getx, setx, delx, "I'm the 'x' property.")

    def test_wrap_access(self):
        class Cell(object):
            def __init__(self, val):
                self._value = val

            def recalc(self):
                self._value = "recalc: " + self._value

            def getvalue(self):
                "Recalculate the cell before returning value"
                self.recalc()
                return self._value

            value = property(getvalue)

        ins = Cell("b10")
        self.assertEqual(ins._value,'b10')
        self.assertEqual(ins.value, "recalc: b10")


if __name__ == "__main__":
    unittest.main()

