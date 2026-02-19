import pytest
from assignment6.util import diff_values
def test_case1():
    assert diff_values(1) == ["1 1 1 1"]


def test_case2():
    assert diff_values(2) == [
        "1 1 1 1",
        "2 2 2 10"
    ]

