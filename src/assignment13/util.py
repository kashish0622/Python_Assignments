import numpy as np
def determinant(matrix):
    x = np.array(matrix, datatype = float)
    d = np.linalg.det(x)
    return round(d, 2)