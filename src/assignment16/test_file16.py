import pytest
from assignment16.util import words
def test_words_basic():
    word_list = ["apple", "banana", "apple", "orange", "banana"]

    unique_count, freq_list = words(word_list)
    assert unique_count == 3
    assert freq_list == [2, 2, 1]