# import pytest
# from code_challenges.fifo_animal_shelter.fifo_animal_shelter.fifo_animal_shelter import Cat,Dog,Animal_Shelter

# def test_add_cat_and_dog_only():
#     shelter = Animal_Shelter()
#     shelter.enqueue("cat")
#     shelter.enqueue("dog")
#     expected = 'cat -> dog'
#     actual = str(shelter)
#     assert actual == expected

# def test_add_another_animal(shelter):
#     shelter.enqueue("horse")
#     expected = 'cat -> cat -> dog -> dog -> cat -> dog -> cat -> dog'
#     actual = str(shelter)
#     assert actual == expected

# def test_dequeue_one_cat(shelter):
#     expected = "cat"
#     actual = shelter.dequeue('cat')
#     assert actual == expected

# def test_dequeue_multiple_cat(shelter):
#     shelter.dequeue('cat')
#     shelter.dequeue('cat')
#     expected = 'dog -> dog -> cat -> dog -> cat -> dog'
#     actual = str(shelter)
#     assert actual == expected

# def test_dequeue_one_dog(shelter):
#     expected = "dog"
#     actual = shelter.dequeue('dog')
#     assert actual == expected

# def test_dequeue_multiple_dog(shelter):
#     shelter.dequeue('dog')
#     shelter.dequeue('dog')
#     expected = 'cat -> cat -> cat -> dog -> cat -> dog'
#     actual = str(shelter)
#     assert actual == expected

# def test_dequeue_another_animal(shelter):
#     actual = shelter.dequeue('horse')
#     assert not actual

# @pytest.fixture
# def shelter():
#     shelter = Animal_Shelter()
#     shelter.enqueue("cat") # -> first cat
#     shelter.enqueue("cat") # -> second cat
#     shelter.enqueue("dog") # -> -> -> first dog
#     shelter.enqueue("dog") # -> -> -> secon dog
#     shelter.enqueue("cat") # -> third cat
#     shelter.enqueue("dog") # -> -> -> third dog
#     shelter.enqueue("cat") # -> forth cat
#     shelter.enqueue("dog") # -> -> -> forth dog
#     # cat -> cat -> dog -> dog -> cat -> dog -> cat -> dog
#     return shelter
