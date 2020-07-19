from testfixtures import TempDirectory
from foo2bar import foo2bar
with TempDirectory() as d:
      d.write('test.txt', b'some foo thing')
      foo2bar(d.path, 'test.txt')
      d.read('test.txt')