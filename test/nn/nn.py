# https://iamtrask.github.io/2015/07/12/basic-python-network/
# A neural network trained with backpropagation is attempting to use input to predict output.
import numpy as np

# sigmoid function
def nonlin(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T


def nn(getInd=False):

    # seed random numbers to make calculation
    # deterministic (just a good practice)
    np.random.seed(1)

    # initialize weights randomly with mean 0
    syn0 = 2 * np.random.random((3, 1)) - 1

    count = 10000
    l1_error=[]
    for iter in range(count):

        # forward propagation
        l0 = X
        l1 = nonlin(np.dot(l0, syn0))

        # how much did we miss?
        temp=l1_error
        l1_error = y - l1
        # if iter==count-1:
        #     print(l1_error-temp)
        # else:
        #     print(l1_error-temp)
        # multiply how much we missed by the
        # slope of the sigmoid at the values in l1
        l1_delta = l1_error * nonlin(l1, True)

        # update weights
        syn0 += np.dot(l0.T, l1_delta)
        if iter == 1 and getInd:

            return {"l1": l1, "l1_error": l1_error}

    # print "Output After Training:"
    return {"l1": l1, "l1_error": l1_error}

