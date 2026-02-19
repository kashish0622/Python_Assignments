import pytest
from assignment19.util import is_valid
def test_validmails():
    assert is_valid("test@example.com") == True
    assert is_valid("kashish123@gmail.in") == True
    assert is_valid("ggits@domain.org") == True
    assert is_valid("nokia@company.net") == True


def test_invalidmails():
    assert is_valid("testexample.com") == False