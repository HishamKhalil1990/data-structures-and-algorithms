import pytest
from code_challenges.left_join.left_join import left_join
from code_challenges.hashtable.hashtable import HashTable

def test_left_join_match(hashtable_one_and_two_no_empty):
    expected = [['fond', 'enamored', 'averse'], ['warth', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'grab', 'Null'], ['guide', 'usher', 'follow']]
    left,right = hashtable_one_and_two_no_empty
    actual = left_join(left,right)
    assert actual == expected

def test_left_join_no_match_right_is_empty(hashtable_one_and_empty):
    expected = [['fond', 'enamored', 'Null'], ['warth', 'anger', 'Null'], ['diligent', 'employed', 'Null'], ['outfit', 'grab', 'Null'], ['guide', 'usher', 'Null']]
    left,right = hashtable_one_and_empty
    actual = left_join(left,right)
    assert actual == expected

def test_left_join_no_match_left_is_empty(hashtable_empty_and_two):
    expected = []
    left,right = hashtable_empty_and_two
    actual = left_join(left,right)
    assert actual == expected

def test_left_join_no_match_both_empty():
    expected = []
    hashtable_one = HashTable()
    hashtable_two = HashTable()
    actual = left_join(hashtable_left=hashtable_one,hashtable_right=hashtable_two)
    assert actual == expected

@pytest.fixture
def hashtable_one_and_two_no_empty():
    hashtable_one = HashTable()
    hashtable_two = HashTable()
    hashtable_one.add('fond','enamored')
    hashtable_one.add('warth','anger')
    hashtable_one.add('diligent','employed')
    hashtable_one.add('outfit','grab')
    hashtable_one.add('guide','usher')
    hashtable_two.add('fond','averse')
    hashtable_two.add('warth','delight')
    hashtable_two.add('diligent','idle')
    hashtable_two.add('guide','follow')
    hashtable_two.add('flow','jam')
    return hashtable_one,hashtable_two

@pytest.fixture
def hashtable_one_and_empty():
    hashtable_one = HashTable()
    hashtable_two = HashTable()
    hashtable_one.add('fond','enamored')
    hashtable_one.add('warth','anger')
    hashtable_one.add('diligent','employed')
    hashtable_one.add('outfit','grab')
    hashtable_one.add('guide','usher')
    return hashtable_one,hashtable_two

@pytest.fixture
def hashtable_empty_and_two():
    hashtable_one = HashTable()
    hashtable_two = HashTable()
    hashtable_two.add('fond','enamored')
    hashtable_two.add('warth','anger')
    hashtable_two.add('diligent','employed')
    hashtable_two.add('outfit','grab')
    hashtable_two.add('guide','usher')
    return hashtable_one,hashtable_two


