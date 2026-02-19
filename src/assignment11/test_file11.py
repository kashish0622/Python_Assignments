import numpy as np
from assignment11.util import fcr


def test_fcr_basic():
    x = [1.2, 2.5, -3.7]

    floor_val, ceil_val, rint_val = fcr(x)

    assert np.array_equal(floor_val, np.array([1., 2., -4.]))
    assert np.array_equal(ceil_val, np.array([2., 3., -3.]))
    assert np.array_equal(rint_val, np.array([1., 2., -4.]))