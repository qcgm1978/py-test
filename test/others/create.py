def main():
    alist=['abs','delattr','hash',
'memoryview',
'set',
'all',
'dict',
'help',
'min',
'setattr',
'any',
'dir',
'hex',
'next',
'slice',
'ascii',
'divmod',
'id',
'object',
'sorted',
'bin',
'enumerate',
'input',
'oct',
'staticmethod',
'bool',
'eval',
'int',
'open',
'str',
'breakpoint',
'exec',
'isinstance',
'ord',
'sum',
'bytearray',
'filter',
'issubclass',
'pow',
'super',
'bytes',
'float',
'iter',
'print',
'tuple',
'callable',
'format',
'len',
'property',
'type',
'chr',
'frozenset',
'list',
'range',
'vars',
'classmethod',
'getattr',
'locals',
'repr',
'zip',
'compile',
'globals',
'map',
'reversed',
'__import__',
'complex',
'hasattr',
'max',
'round']
    for item in alist:
        f= open('test/library1/'+item+".py","w+")
        # for i in range(10):
        #      f.write("This is line %d\r\n" % (i+1))
        content ='''
import unittest
class TDD{0}(unittest.TestCase):
    def test_{0}(self):
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

                '''
        f.write(content.format(item))
        f.close()
        
if __name__ == '__main__':
    main()
