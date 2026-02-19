from assignment8.util import dayofweek
def test_dayofweek_leap_year():
    assert dayofweek("2020-02-29") == "Saturday"
def test_dayofweek_today():
    assert dayofweek("2026-02-19") == "Thursday"