import numpy as np
def min_max(values):
    x = np.array(values, datatype = int)
    min_axis = np.min(x, axis = 1)
    return np.max(min_axis)