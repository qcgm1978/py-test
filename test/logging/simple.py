
import unittest, logging
logging.getLogger().setLevel(logging.INFO)
class TDD_SIMPLE(unittest.TestCase):
    def test_simple(self):
        # getattr(logging, loglevel.upper())

        logging.warning('Watch out!')  # will print a message to the console
        logging.info('I told you so')  # will not print anything
    def test_logging_file(self):
        # logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
if __name__ == '__main__':
    unittest.main()

                