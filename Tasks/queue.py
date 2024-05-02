


# you can use the built-in queue module to implement queues.
# The queue module provides the Queue class, which is a first-in, first-out (FIFO) data structure

#
# from queue import Queue
from queue import Queue

my_queue = Queue()

my_queue.put(1)
my_queue.put(2)
my_queue.put(3)


first_element = my_queue.get()
second_element = my_queue.get()

print("Dequeued elements:", first_element, second_element)
