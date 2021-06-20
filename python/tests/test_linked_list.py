# import pytest
# from code_challenges.Data_Structures.linked_list.linked_list.linked_list import Linked_List

# def test_import():
#     assert Linked_List

# def test_create_an_empty_linked_list():
#     expected = 'empty'
#     actual = str(Linked_List())
#     assert actual == expected

# def test_head_pointer(linked_instance):
#     expected = 'chair'
#     actual = str(linked_instance.head)
#     assert actual == expected

# def test_can_insert():
#     expected = 'home is inserted'
#     actual = Linked_List().insert('home')
#     assert actual == expected

# def text_can_insert_more_than_one():
#     expected = ['home is inserted','car is inserted','laptop is inserted']
#     linked_ins = Linked_List()
#     actual = [linked_ins.insert('home'),linked_ins.insert('car'),linked_ins.insert('laptop')]
#     assert actual == expected

# def test_found_item(linked_instance):
#     assert linked_instance.includes('plane')

# def test_not_found_item(linked_instance):
#     assert not linked_instance.includes('dog')

# def test_collection_data(linked_instance):
#     expected = "head -> {chair} -> {table} -> {cat} -> {bike} -> {laptop} -> {plane} -> {home} -> {car} -> X"
#     actual = str(linked_instance)
#     print(actual)
#     assert actual == expected

# def test_append1(linked_instance2):
#     expected = "head -> [1] -> [3] -> [2] -> [5] -> X"
#     linked = linked_instance2
#     linked.append(5)
#     actual = str(linked)
#     assert actual == expected

# def test_append2():
#     expected = "head -> [1] -> X"
#     linked = Linked_List()
#     linked.append(1)
#     actual = str(linked)
#     assert actual == expected

# def test_append_multiple(linked_instance2):
#     expected = "head -> [1] -> [3] -> [2] -> [5] -> [6] -> X"
#     linked = linked_instance2
#     linked.append(5)
#     linked.append(6)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_before1(linked_instance2):
#     expected = "head -> [1] -> [5] -> [3] -> [2] -> X"
#     linked = linked_instance2
#     linked.insert_before(3,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_before_head(linked_instance2):
#     expected = "head -> [5] -> [1] -> [3] -> [2] -> X"
#     linked = linked_instance2
#     linked.insert_before(1,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_before3(linked_instance3):
#     expected = "head -> [1] -> [5] -> [2] -> [2] -> X"
#     linked = linked_instance3
#     linked.insert_before(2,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_before4(linked_instance2):
#     with pytest.raises(ValueError):
#         linked_instance2.insert_before(4,5)

# def test_insert_after1(linked_instance2):
#     expected = "head -> [1] -> [3] -> [5] -> [2] -> X"
#     linked = linked_instance2
#     linked.insert_after(3,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_after2(linked_instance2):
#     expected = "head -> [1] -> [5] -> [3] -> [2] -> X"
#     linked = linked_instance2
#     linked.insert_after(1,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_after3(linked_instance3):
#     expected = "head -> [1] -> [2] -> [5] -> [2] -> X"
#     linked = linked_instance3
#     linked.insert_after(2,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_after_end(linked_instance2):
#     expected = "head -> [1] -> [3] -> [2] -> [5] -> X"
#     linked = linked_instance2
#     linked.insert_after(2,5)
#     actual = str(linked)
#     assert actual == expected

# def test_insert_after4(linked_instance2):
#     with pytest.raises(ValueError):
#         linked_instance2.insert_after(4,5)

# def test_kth_from_end_1(linked_instance4):
#     excepted = 2
#     actual = linked_instance4.kth_from_end(0)
#     assert actual == excepted

# def test_kth_from_end_2(linked_instance4):
#     excepted = 3
#     actual = linked_instance4.kth_from_end(2)
#     assert actual == excepted

# def test_kth_from_end_3(linked_instance4):
#     excepted = 7
#     actual = linked_instance4.kth_from_end(4)
#     assert actual == excepted

# def test_kth_from_end_4(linked_instance4):
#     excepted = 10
#     actual = linked_instance4.kth_from_end(7)
#     assert actual == excepted

# def test_kth_from_end_5(linked_instance4):
#     with pytest.raises(ValueError):
#         linked_instance4.kth_from_end(9)

# def test_kth_from_end_6():
#     linked = Linked_List()
#     with pytest.raises(ValueError):
#         linked.kth_from_end(0)

# def test_kth_from_end_7():
#     linked = Linked_List()
#     with pytest.raises(ValueError):
#         linked.kth_from_end('a')

# @pytest.fixture
# def linked_instance():
#     linked = Linked_List()
#     linked.insert('car')
#     linked.insert('home')
#     linked.insert('plane')
#     linked.insert('laptop')
#     linked.insert('bike')
#     linked.insert('cat')
#     linked.insert('table')
#     linked.insert('chair')
#     return linked

# @pytest.fixture
# def linked_instance2():
#     linked = Linked_List()
#     linked.insert(2)
#     linked.insert(3)
#     linked.insert(1)
#     return linked

# @pytest.fixture
# def linked_instance3():
#     linked = Linked_List()
#     linked.insert(2)
#     linked.insert(2)
#     linked.insert(1)
#     return linked

# @pytest.fixture
# def linked_instance4():
#     linked = Linked_List()
#     linked.insert(2)
#     linked.insert(8)
#     linked.insert(3)
#     linked.insert(1)
#     linked.insert(7)
#     linked.insert(9)
#     linked.insert(11)
#     linked.insert(10)
#     return linked
