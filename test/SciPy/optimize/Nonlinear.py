import numpy as np
def F(x):
    return np.cos(x) + x[::-1] - [1, 2, 3, 4]
import scipy.optimize
x = scipy.optimize.broyden1(F, [1,1,1,1], f_tol=1e-14)
print x
# array([ 4.04674914,  3.91158389,  2.71791677,  1.61756251])
np.cos(x) + x[::-1]