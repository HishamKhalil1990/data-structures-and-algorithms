import pytest
from code_challenges.hashtable.hashtable import HashTable

def test_adding_to_hashtable():
    expected = ['car','BMW']
    hashtable = HashTable()
    actual = hashtable.add('car','BMW')
    assert actual == expected

def test_get_existed_key():
    expected = 'python'
    hashtable = HashTable()
    hashtable.add('Dario','python')
    actual = hashtable.get('Dario')
    assert actual == expected

def test_get_not_existed_key():
    expected = None
    hashtable = HashTable()
    hashtable.add('Dario','python')
    actual = hashtable.get('hisham')
    assert actual == expected

def test_handle_collisons():
    expected = 'head -> {["dario", "python"]} -> {["radio", "hala-fm"]} -> X'
    hashtable = HashTable()
    hashtable.add("dario","python")
    hashtable.add("radio","hala-fm")
    for bucket in hashtable._buckets:
        if bucket:
            actual = str(bucket).replace('\'','"')
    assert actual == expected

def test_get_value_for_collisons_bucket():
    expected = ['python','hala-fm']
    hashtable = HashTable()
    hashtable.add('dario','python')
    hashtable.add('radio','hala-fm')
    actual = [hashtable.get('dario'),hashtable.get('radio')]
    assert actual == expected

def test_conatin_key_true():
    hashtable = HashTable()
    hashtable.add('dario','python')
    actual = hashtable.contains('dario')
    assert actual

def test_conatin_key_False():
    hashtable = HashTable()
    hashtable.add('dario','python')
    actual = hashtable.contains('hisham')
    assert not actual

def test_hash_key_in_range():
    expected  = 1024
    hashtable = HashTable()
    actual = hashtable._hash('house')
    assert actual in range(expected)
