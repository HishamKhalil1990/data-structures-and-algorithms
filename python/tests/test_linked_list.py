import pytest
from code_challenges.Data_Structures.linked_list.linked_list.linked_list import Node,Linked_List


def test_import():
    assert Linked_List

def test_create_an_empty_linked_list():
    expected = 'empty'
    actual = str(Linked_List())
    assert actual == expected

def test_head_pointer(liked_instance):
    expected = 'chair'
    actual = str(liked_instance.head)
    assert actual == expected

def test_can_insert():
    expected = 'home is inserted'
    actual = Linked_List().insert('home')
    assert actual == expected

def text_can_insert_more_than_one():
    expected = ['home is inserted','car is inserted','laptop is inserted']
    linked_ins = Linked_List()
    actual = [linked_ins.insert('home'),linked_ins.insert('car'),linked_ins.insert('laptop')]
    assert actual == expected

def test_found_item(liked_instance):
    assert liked_instance.includes('plane')

def test_not_found_item(liked_instance):
    assert not liked_instance.includes('dog')

def test_collection_data(liked_instance):
    expected = "{chair} -> {table} -> {cat} -> {bike} -> {laptop} -> {plane} -> {home} -> {car} -> Null"
    actual = str(liked_instance)
    print(actual)
    assert actual == expected

@pytest.fixture
def liked_instance():
    linked = Linked_List()
    linked.insert('car')
    linked.insert('home')
    linked.insert('plane')
    linked.insert('laptop')
    linked.insert('bike')
    linked.insert('cat')
    linked.insert('table')
    linked.insert('chair')
    return linked
