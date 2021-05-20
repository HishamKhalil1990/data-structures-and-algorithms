# Stacks and Queues
### Stacks and Queues are a simple data structure, one of the advantages of them is their big O is 1. however the only difference between them is for stacks, the concept is First In Last Out (FILO) and for the Queue, the concept is First In First Out (FIFO)

## Challenge
### the challenge is to create a Stack class to connect nodes in one direction where the new added node is put at the top and all methods are applied at the top node and create a Queue class to connect nodes in one direction where the new added node is put in rear except the first node is put in front and all methods are applied at the top node

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### i create the Stack class to add a given value in a node, assign the existed top as a next to the node and put the node as top, the nodes are connected to each other in one direction. i create the Queue class to add a given value in a node, assign the existed rear as a next to the node and put the node as rear except for the first node it will be added to front, the nodes are connected to each other in one direction
### Big O is 1

## API
<!-- Description of each method publicly available to your Stack and Queue-->
- Stack:
    - `push` takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
    - `pop` takes no argument, removes the node from the top of the stack, and returns the node’s value and should raise exception when called on empty stack
    - `peek` takes no argument and returns the value of the node located on top of the stack, without removing it from the stack and should raise exception when called on empty stack
    - `is_empty` takes no argument, and returns a boolean indicating whether or not the stack is empty.
- Queue:
    - `enqueue` takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
    - `dequeue` takes no argument, removes the node from the front of the queue, and returns the node’s value and should raise exception when called on empty queue
    - `peek` take no argument and returns the value of the node located in the front of the queue, without removing it from the queue and should raise exception when called on empty queue
    - `is_empty` takes no argument, and returns a boolean indicating whether or not the queue is empty.

PR link https://github.com/HishamKhalil1990/data-structures-and-algorithms/pull/32
