# Plot y versus x as lines and/or markers.
import matplotlib.pyplot as plt
plot=plt.plot
import unittest
class TDD_PLOT(unittest.TestCase):
    def test_plot(self):
        plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
        plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')
        plt.show()
if __name__ == '__main__':
    unittest.main()

                