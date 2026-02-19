import pytest
from assignment15.util import happiness
def test_case1():
    array = [1, 5, 3]
    setA = {3, 1}
    setB = {5, 7}
    assert happiness(array, setA, setB) == 1


def test_case2():
    array = [1, 2, 3]
    setA = {1, 2, 3}
    setB = {4, 5}
    assert happiness(array, setA, setB) == 3

