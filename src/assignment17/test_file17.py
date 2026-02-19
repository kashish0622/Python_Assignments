import pytest
from assignment17.util import block


def test_block_possible():
    cubes = [4, 3, 2, 1, 3, 4]
    assert block(cubes) == True
def test_block_not_possible():
    cubes = [1, 3, 2]
    assert block(cubes) == False