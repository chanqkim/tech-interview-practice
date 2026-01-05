from collections import deque

"""
# Performance comparison for dequeue function
## list.pop(0) = O(n)
- Python list is implemented as a dynamic array
- Removing the first element (index 0) requires shifting all remaining elements one position to the left(linear)

## deque.popleft() = O(1)
- deque is implemented as a doubly linked list of fixed-size blocks
- Removing elements from either end does not require shifting
    - Only pointer adjustments are needed

# Interview Tip
- Use collections.deque instead of list when implementing a queue in Python as pop(0) is O(n) while popleft() is O(1).
- list-based queue is acceptable only when dequeue operations are rare or input size is small
- deque is preferred for BFS, simulation, and queue-heavy problems
"""


# Basic Queue implementation using a list
class Queue:
    def __init__(self):
        self.items = []

    # Add item to a queue (FIFO)
    def enqueue(self, value):
        self.items.append(value)

    # Remove and return item from a queue (FIFO)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")

        return self.items.pop(0)

    # Check the front item of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            return self.items[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the size of the queue
    def queue_size(self):
        return len(self.items)


# Queue implementation using deque for better performance
class DequeQueue:
    def __init__(self):
        self.items = deque()

    # Add item to a queue (FIFO)
    def enqueue(self, value):
        self.items.append(value)

    # Remove and return item from a queue (FIFO)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue(deque) is empty!")
        return self.items.popleft()

    # Check the front item of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise Exception("Queue(deque) is empty!")
        return self.items[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the size of the queue
    def queue_size(self):
        return len(self.items)
