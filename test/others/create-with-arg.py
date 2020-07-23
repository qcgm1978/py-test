import sys
print(sys.argv)
def main():
    alist = [
       sys.argv[1]
    ]
    for item in alist:
        f = open(sys.argv[2] + item + ".py", "w+")
        # for i in range(10):
        #      f.write("This is line %d\r\n" % (i+1))
        content = """
import unittest
class TDD{0}(unittest.TestCase):
    def test_{0}(self):
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

                """
        f.write(content.format(item))
        f.close()


if __name__ == "__main__":
    main()
