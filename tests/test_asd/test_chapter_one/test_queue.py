from asd.chapter_one.queue import Queue, split_queue


def test_enqueue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')
    assert queue.queue[0] == "one"


def test_dequeue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')
    queue.dequeue()
    assert queue.size() == 2
    assert queue.queue[0] == "two"


def test_split_queue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')
    queue.enqueue('four')
    queue.enqueue('five')
    split_queue(3, queue)
    assert queue.queue[0] == "four"
