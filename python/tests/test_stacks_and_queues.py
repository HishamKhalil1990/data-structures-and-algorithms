import pytest
from code_challenges.stacks_and_queues.stacks_and_queues.stacks_and_queues import Stack,Queue,EmptySatckException,EmptyQueueException

def test_stack_push_one():
    expected = "5 "
    stack = Stack()
    stack.push(5)
    actual = str(stack)
    assert actual == expected

def test_stack_multiple_push(stacked):
    expected = "2 3 4 5 "
    actual = str(stacked)
    assert actual == expected

def test_stack_pop_one(stacked):
    expected = 2
    actual = stacked.pop()
    assert actual == expected

def test_stack_multiple_pop(stacked):
    for num in range(4):
        stacked.pop()
    with pytest.raises(EmptySatckException):
        stacked.pop()

def test_stack_peek_top(stacked):
    expected = 1
    stacked.push(1)
    actual = stacked.peek()
    assert actual == expected

def test_instantiate_empty_stack():
    stack = Stack()
    actual = stack.is_empty
    assert actual

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(EmptySatckException):
        stack.peek()
    with pytest.raises(EmptySatckException):
        stack.pop()

def test_queue_enqueue_one():
    expected = "5 "
    queue = Queue()
    queue.enqueue(5)
    actual = str(queue)
    assert actual == expected

def test_queue_multiple_enqueue(queued):
    expected = "5 4 3 2 "
    actual = str(queued)
    assert actual == expected

def test_queue_dequeue_one(queued):
    expected = 5
    actual = queued.dequeue()
    assert actual == expected

def test_queue_multiple_dequeue(queued):
    for num in range(4):
        queued.dequeue()
    with pytest.raises(EmptyQueueException):
        queued.dequeue()

def test_queue_peek_front(queued):
    expected = 5
    actual = queued.peek()
    assert actual == expected

def test_instantiate_empty_queue():
    queue = Queue()
    actual = queue.is_empty
    assert actual

def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(EmptyQueueException):
        queue.peek()
    with pytest.raises(EmptyQueueException):
        queue.dequeue()

@pytest.fixture
def stacked():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    return stack

@pytest.fixture
def queued():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    return queue
