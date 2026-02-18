import numpy as np
def min_max(matrix):
    x = np.array(matrix, datatype = int)
    min_axis = np.min(x, axis = 1)
    return np.max(min_axis)