
import unittest
import numpy as np
from get_linspace import linspace
import matplotlib.pyplot as plt
class TDD_LINSPACE(unittest.TestCase):
    def test_linspace(self):
        l=np.linspace(2.0, 3.0, num=5)
        l1=linspace(2.0, 3.0, num=5)
        self.assertEqual(list(l),[2.  , 2.25, 2.5 , 2.75, 3.  ])
        self.assertEqual(l1,[2.  , 2.25, 2.5 , 2.75, 3.  ])
        l2=np.linspace(2.0, 3.0, num=5, endpoint=False)
        l3=linspace(2.0, 3.0, num=5, endpoint=False)
        self.assertEqual(list(l2),[2. ,  2.2,  2.4,  2.6,  2.8])
        self.assertEqual(l3,[2. ,  2.2,  2.4,  2.6,  2.8])
        l4=np.linspace(2.0, 3.0, num=5, retstep=True)
        l5=linspace(2.0, 3.0, num=5, retstep=True)
        self.assertEqual(len(list(l4)),2)
        self.assertFalse((list(l4)[0] - [2., 2.25, 2.5, 2.75, 3.]).any())
        self.assertEqual(list(l4)[1],.25)
        self.assertEqual(l5, ([2.0, 2.25, 2.5, 2.75, 3.0], 4))
    def test_graphical(self):
        N = 8
        y = np.zeros(N)
        self.assertEqual(list(y),[0,0,0,0,0,0,0,0])
        x1 = np.linspace(0, 10, N, endpoint=True)
        x1_1 = linspace(0, 10, N, endpoint=True)
        self.assertEqual(list(x1),x1_1)
        x2 = np.linspace(0, 10, N, endpoint=False)
        x2_2 = linspace(0, 10, N, endpoint=False)
        self.assertEqual(list(x2),x2_2)
        plt.plot(x1, y, 'o')
        # plt.plot(x2, y + 0.5, 'o')
        # plt.ylim([-0.5, 1])
        # (-0.5, 1)
        # plt.show()
if __name__ == '__main__':
    unittest.main()

                