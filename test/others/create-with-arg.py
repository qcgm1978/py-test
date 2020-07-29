import sys
print(sys.argv)
def main():
    alist = [
       [sys.argv[1].split('/')[-1].upper(),
       sys.argv[1].split('/')[-1]]
    ]
    for item in alist:
        f = open(sys.argv[1] + ".py", "w+")
        # for i in range(10):
        #      f.write("This is line %d\r\n" % (i+1))
        content = """
import unittest
class TDD_{0}(unittest.TestCase):
    def test_{1}(self):
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

                """
        f.write(content.format(item[0],item[1]))
        f.close()


if __name__ == "__main__":
    main()
