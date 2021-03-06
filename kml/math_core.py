import numpy as np

def wavg(elements, weights):
    """ Finds weighted average """
    r = 0
    sum = np.sum(weights)
    for x,w in zip(elements, weights):
        r += x*w / sum
    return r

class Kernel:
    """
    All kernels for smoothing here
    http://ru.learnmachinelearning.wikia.com/wiki/Ядерное_сглаживание_для_оценки_плотности
    """
    @staticmethod
    def Gaussian(x):
        return 1. / np.sqrt(2 * np.pi) * np.exp(- x**2 / 2)

    @staticmethod
    def Epanechnikov(x):
        return 3. / 4. * max(1. - x**2, 0)

    @staticmethod
    def Rectangular(x):
        if(abs(x)<=1):
            return 1./2.;
        else:
            return 0;

class Norm:
    """
    Some norms
    """
    @staticmethod
    def e(x):
        return np.sqrt(np.sum(x**2))

class Metric:
    """
    Some metrics in linear space (etc ||a-b||)
    """
    @staticmethod
    def Euclidean(a, b):
        return Norm.e(a-b)
