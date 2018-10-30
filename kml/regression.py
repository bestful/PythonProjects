from kml.math_core import *
import numpy as np

def Weights(el, X, Y, h, kernel, metric, **kwargs):
    W = np.array([])
    for x in X:
        W = np.append(W, [kernel(metric(el, x) / h)])
    return W

def NodorayWatson(el, X, Y, h, kernel=Kernel.Epanechnikov, metric=Metric.Euclidean, **kwargs):
    if 'weights' in kwargs:
        W = kwargs['weights']
    else:
        W = Weights(**locals())

    return wavg(elements=Y, weights=W)
    """ Need to write (error)
    if kernel(1) == 0:
        cut = [W > 0]
        print(cut)
        W, Y = W[cut], Y[cut]
        return wavg(elements=Y, weights=W)

    r = 0
    sum = np.sum(W)
    for y,w in zip(Y,W):
        r += y*w / sum
    return r
    """

def LOWESS(X, Y, h, eps=0.001, sigma=1, gamma_kernel=Kernel.Gaussian, **kwargs):
    l = Y.size
    gamma_new = np.repeat(1, l)
    condition = True

    while condition:
        gamma_old = gamma_new
        a = np.repeat(0, l)

        for i in range(l):
            x_i, y_i, gamma_i = np.delete(X, i), np.delete(Y, i), np.delete(gamma_new, i)
            W_i = Weights(el = X[i], X=x_i, Y=y_i, h=h, **kwargs)
            a[i] = NodorayWatson(el=X[i], X=x_i, Y=y_i, h=h, weights=W_i*gamma_i, **kwargs)
	
        a_y = np.abs(a-Y)
        med = np.median(a_y)
        gamma_new = np.array([gamma_kernel(a_y[i]/med/sigma) for i in range(0,l)])

        if np.linalg.norm(gamma_new-gamma_old)<eps:
            condition = False
    return gamma_new

