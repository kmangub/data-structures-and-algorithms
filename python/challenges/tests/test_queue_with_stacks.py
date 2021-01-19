import pytest
from challenges.queue_with_stacks.queue_with_stacks import PseudoQueue, Stack, Node, InvalidOperationError

def test_dequeue_from_example():
    pq = PseudoQueue()
    pq.enqueue(5)
    pq.enqueue(3)
    pq.enqueue(1)
    actual = pq.dequeue()
    expected = 5
    assert actual == expected

    