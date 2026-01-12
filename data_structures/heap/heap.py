"""
Heap Data Structure Implementation
- A complete binary tree where each parent node is greater than or equal to its child nodes (max-heap)
- Efficiently supports insertion and removal of the maximum element
- Commonly used in priority queues and heap sort algorithms

- Time Complexity:
  - Insertion (push): O(log n)
    - height of the tree is log n, need to traverse(each stage is O(1)) from leaf to root
  - Removal (pop): O(log n)
     - height of the tree is log n, need to traverse(each stage is O(1)) from leaf to root
  - Peek (max, getting left/right child): O(1)
- Space Complexity: O(n) for storing n elements in the heap
"""


class Heap:
    def __init__(self):
        # initialize an empty list to store heap elements
        self.heap = []

    # add a new value to the heap and maintain heap property
    def push(self, value):
        # add value to the end of the heap
        self.heap.append(value)

        # restore heap property by moving the value upward
        last_index = len(self.heap) - 1
        self._heapify_up(last_index)

    # remove and return the root value from the heap and maintain heap property
    def pop(self):
        if not self.heap:
            raise Exception("Heap is empty!")

        last_value = self.heap.pop()  # Remove and store the last value
        root_value = self.heap[0]  # Store the root value to return later
        self.heap[0] = last_value  # Move the last value to the root

        # Rrstore heap property by moving the root value downward
        self._heapify_down(0)

        return root_value

    # return the size of the heap
    def size(self):
        return len(self.heap)

    # rebalance the heap upwards from a given index
    def _heapify_up(self, index):
        # compare current value with the parent node and swap value

        while index > 0:
            # check
            parent = (index - 1) // 2

            if self.heqp[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    # rebalance the heap downwards from a given index
    def _heapify_down(self, index):
        # compare current value with child nodes and swap value
        while True:
            # find left and right child indices
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # swap largest value with left child node if left child node value is larger
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left

            # swap largest value with right child node if right child node value is larger
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            # if largest_value is not a root node, swap and continue heapifying down
            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                index = largest
            else:
                break

    # return the index of the parent node
    def _parent(self, index):
        return (index - 1) // 2

    # return the index of the left child node
    def _left_child(self, index):
        return 2 * index + 1

    # return the index of the right child node
    def _right_child(self, index):
        return 2 * index + 2
