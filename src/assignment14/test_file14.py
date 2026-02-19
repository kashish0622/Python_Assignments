import numpy as np
from assignment14.util import mean
def test_mean_single_row():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    mean_axis, variance_axis, standard_axis = mean(matrix)

    assert np.allclose(mean_axis, np.array([1.5, 3.5]))
    assert np.allclose(variance_axis, np.array([1.0, 1.0]))
    assert round(standard_axis, 3) == 1.118
