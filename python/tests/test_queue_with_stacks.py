import pytest
from code_challenges.queue_with_stacks.queue_with_stacks.queue_with_stacks import Pseudo_Queue
from code_challenges.stacks_and_queues.stacks_and_queues.stacks_and_queues import EmptyQueueException

def test_Pseudo_Queue_enqueue_for_empty():
    expected = "[5]"
    queue = Pseudo_Queue()
    queue.enqueue(5)
    actual = str(queue)
    assert actual == expected

def test_Pseudo_Queue_enqueue_for_non_empty(queued):
    expected = "[5]->[20]->[15]->[10]"
    queued.enqueue(5)
    actual = str(queued)
    assert actual == expected

def test_Pseudo_Queue_dequeue_one(queued):
    expected = "[5]->[20]->[15]"
    queued.enqueue(5)
    queued.dequeue()
    actual = str(queued)
    assert actual == expected

def test_Pseudo_Queue_dequeue_two(queued):
    expected = "[5]->[20]"
    queued.enqueue(5)
    queued.dequeue()
    queued.dequeue()
    actual = str(queued)
    assert actual == expected

@pytest.fixture
def queued():
    queue = Pseudo_Queue()
    queue.enqueue(10) # first in --> first out
    queue.enqueue(15) # second in --> second out
    queue.enqueue(20) # third in --> third out
    return queue

