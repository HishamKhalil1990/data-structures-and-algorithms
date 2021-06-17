# import pytest
# from code_challenges.quick_sort.quick_sort import quickSort

# def test_quickSort_integers_values_one():
#     expected = [4, 8, 15, 16, 23, 42]
#     actual = quickSort([8,4,23,42,16,15],0,5)
#     assert actual == expected

# def test_quickSort_integers_values_two():
#     expected = [-2, 5, 8, 12, 18, 20]
#     actual = quickSort([20,18,12,8,5,-2],0,5)
#     assert actual == expected

# def test_quickSort_integers_values_three():
#     expected = [5, 5, 5, 7, 7, 12]
#     actual = quickSort([5,12,7,5,5,7],0,5)
#     assert actual == expected

# def test_quickSort_integers_empty_list():
#     expected = []
#     actual = quickSort([],0,-1)
#     assert actual == expected

# def test_quickSort_non_integers_values():
#     with pytest.raises(TypeError):
#         quickSort([10,5,2,7,0,'three'],0,5)
