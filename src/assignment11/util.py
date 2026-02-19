import numpy as np
def fcr(x):
    a = np.array(x, dtype = float)
    return np.floor(a), np.ceil(a), np.rint(a)

