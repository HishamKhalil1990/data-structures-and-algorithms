import pytest
from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_integers_values_one():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort([8,4,23,42,16,15])
    assert actual == expected

def test_insertion_sort_integers_values_two():
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort([20,18,12,8,5,-2])
    assert actual == expected

def test_insertion_sort_integers_values_three():
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort([5,12,7,5,5,7])
    assert actual == expected

def test_insertion_sort_integers_empty_list():
    expected = []
    actual = insertion_sort([])
    assert actual == expected

def test_insertion_sort_non_integers_values():
    with pytest.raises(TypeError):
        insertion_sort([10,5,2,7,0,'three'])
