import numpy as np
def mean(matrix):
    x = np.array(matrix, datatype = float)
    mean_axis = np.mean(x, axis=1)
    variance_axis = np.var(x, axis=0)
    standard_axis = np.std(x, axis=None)
    return mean_axis, variance_axis, standard_axis