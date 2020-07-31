import sys,os

print(sys.argv)


def main():
    l = sys.argv[1].split("/")
    alist = [[l[-1].upper(), l[-1]]]
    dirName = '/'.join(l[:-1])
    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
    for item in alist:
        f = open(sys.argv[1] + ".py", "w+")
        # for i in range(10):
        #      f.write("This is line %d\r\n" % (i+1))
        content = """
import unittest
class TDD_{0}(unittest.TestCase):
    def test_{1}(self):

if __name__ == '__main__':
    unittest.main()

                """
        f.write(content.format(item[0], item[1]))
        f.close()


if __name__ == "__main__":
    main()
