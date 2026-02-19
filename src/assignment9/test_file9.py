import pytest
from assignment9.util import marks
def test_marks_basic():
    n = 3
    columns = ["ID", "MARKS", "NAME", "CLASS"]

    rows = [
        "1 90 John 10",
        "2 80 Alice 10",
        "3 70 Bob 10"
    ]

    result = marks(n, columns, rows)

    assert result == 80.0

def test_marks_single_student():
    n = 1
    columns = ["ID", "MARKS", "NAME", "CLASS"]

    rows = [
        "1 95 Kashish 12"
    ]

    result = marks(n, columns, rows)

    assert result == 95.0


def test_marks_all_same():
    n = 4
    columns = ["ID", "MARKS", "NAME", "CLASS"]

    rows = [
        "1 50 A 9",
        "2 50 B 9",
        "3 50 C 9",
        "4 50 D 9"
    ]

    result = marks(n, columns, rows)

    assert result == 50.0
