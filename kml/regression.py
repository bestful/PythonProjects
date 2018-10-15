from kml.math_core import *
import numpy as np

def NodorayWatson(el, X, Y, h, kernel=Kernel.Epanechnikov, metric=Metric.Euclidean):
    W = np.array([[]])
    r = 0
    for i in X:
        W = np.append(W, [kernel(metric(el, i) / h)])
    sum = np.sum(W)
    for i in Y:
        r = r + i*W[0] / sum
        W = W[1:]
    return r
    """ Need to write (error)
    if kernel(1) == 0:
        cut = [W > 0]
        print(cut)
        W, Y = W[cut], Y[cut]
        return wavg(elements=Y, weights=W)
    """

