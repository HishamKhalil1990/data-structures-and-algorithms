from code_challenges.Data_Structures.linked_list.linked_list.linked_list import Linked_List
from code_challenges.ll_zip.ll_zip.ll_zip import zip_Lists

def test_first_list_is_bigger():
    list1 = Linked_List()
    list1.insert(10)
    list1.insert(9)
    list1.insert(2)
    list1.insert(3)
    list2 = Linked_List()
    list2.insert(5)
    list2.insert(1)
    actual = zip_Lists(list1,list2)
    expected = "head -> [3] -> [1] -> [2] -> [5] -> [9] -> [10] -> X"
    assert actual == expected

def test_second_list_is_bigger():
    list1 = Linked_List()
    list1.insert(2)
    list1.insert(3)
    list2 = Linked_List()
    list2.insert(10)
    list2.insert(7)
    list2.insert(6)
    list2.insert(5)
    list2.insert(1)
    actual = zip_Lists(list1,list2)
    expected = "head -> [3] -> [1] -> [2] -> [5] -> [6] -> [7] -> [10] -> X"
    assert actual == expected

def test_first_list_is_equal_to_second_list():
    list1 = Linked_List()
    list1.insert(2)
    list1.insert(3)
    list2 = Linked_List()
    list2.insert(10)
    list2.insert(7)
    actual = zip_Lists(list1,list2)
    expected = "head -> [3] -> [7] -> [2] -> [10] -> X"
    assert actual == expected
