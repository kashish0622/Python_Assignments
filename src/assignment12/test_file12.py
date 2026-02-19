import numpy as np
from assignment12.util import min_max
def test_min_max_basic():
    values = [
        [2, 5, 1],
        [7, 3, 9],
        [4, 6, 8]
    ]
    assert min_max(values) == 4