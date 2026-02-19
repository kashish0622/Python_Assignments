import pytest
from assignment10.util import time_diff
def test_time_diff_different_timezone():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
def test_time_diff_one_hour():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 14:54:36 -0700"