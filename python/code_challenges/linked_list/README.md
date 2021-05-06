# linked list
### it is a a class used to construct a linked list data structure

## Challenge
### the challenge was to create two classes, one for nodes and one for the linked list and test the classes API

## Approach & Efficiency
### i create the class to behave as single linked list, the nodes are connected to each other in one direction. each node pointer to the next node only
### Big O is leniar

## API
#### Linked_list class:
- `__init__` the class constructor which use to create instances
- `insert` takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- `includes` takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- `__str__` takes in no arguments and returns a string representing all the values in the Linked List
#### Node class:
- `__init__` the class constructor which use to create instances
- `__str__` takes in no arguments and returns a string representing the node data
