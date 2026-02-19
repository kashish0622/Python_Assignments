import numpy as np
from assignment13.util import determinant
def test_determinant_2x2():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert determinant(matrix) == -2.0