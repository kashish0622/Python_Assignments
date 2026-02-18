from util import mutate_string
def test_questionstring():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"
def test_case1():
    assert mutate_string("123456709", 7, "8") == "123456789"