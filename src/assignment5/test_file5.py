from util import mergetools
def test_sample_case():
    assert mergetools("AABCAAADA", 3) == ["AB", "CA", "AD"]
def test_unique_characters():
    assert mergetools("ABCDEF", 3) == ["ABC", "DEF"]

