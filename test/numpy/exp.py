
import unittest
import numpy as np
import matplotlib.pyplot as plt
# Calculate the exponential of all elements in the input array.
class TDD_EXP(unittest.TestCase):
    def test_exp(self):
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        xx = x + 1j * x[:, np.newaxis] # a + ib over complex plane
        out = np.exp(xx)
        print(out)

if __name__ == '__main__':
    unittest.main()

                