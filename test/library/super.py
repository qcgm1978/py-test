
import unittest
class TDDsuper(unittest.TestCase):
    def test_super(self):
        # Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.
        import logging
        # The root logger always defaults to WARNING level. Try calling
        logging.getLogger().setLevel(logging.INFO)
        class LoggingDict(dict):
            def __setitem__(self, key, value):
                logging.info('Setting %r to %r' % (key, value))
                super().__setitem__(key, value)
                return True
        log=LoggingDict()
        self.assertTrue(log.__setitem__('key','value'))
        self.assertEqual(log['key'],'value')
if __name__ == '__main__':
    unittest.main()

                