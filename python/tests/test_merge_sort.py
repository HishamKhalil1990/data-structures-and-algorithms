import pytest
from code_challenges.merge_sort.merge_sort import mergesort

def test_mergesort_integers_values_one():
    expected = [4, 8, 15, 16, 23, 42]
    actual = mergesort([8,4,23,42,16,15])
    assert actual == expected

def test_mergesort_integers_values_two():
    expected = [-2, 5, 8, 12, 18, 20]
    actual = mergesort([20,18,12,8,5,-2])
    assert actual == expected

def test_mergesort_integers_values_three():
    expected = [5, 5, 5, 7, 7, 12]
    actual = mergesort([5,12,7,5,5,7])
    assert actual == expected

def test_mergesort_integers_empty_list():
    expected = []
    actual = mergesort([])
    assert actual == expected

def test_mergesort_non_integers_values():
    with pytest.raises(TypeError):
        mergesort([10,5,2,7,0,'three'])
