class Stack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    # add item to the stack if stack is not full
    def push(self, value):
        if len(self.items) == self.capacity:
            raise Exception("Stack is already Full!")
        self.items.append(value)

    # pop item from the stack if stack is not empty
    def pop(self):
        # if stack is empty
        if len(self.items) == 0:
            raise Exception("Nothing to Pop!")
        # remove top item
        self.items.pop()

    # check if stack is empty and return top item
    def peek(self):
        if len(self.items) == 0:
            raise Exception("stack is empty")
        return self.items[-1]

    # return true if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # return size of the stack
    def size(self):
        return len(self.items)

    # return true if stack is full
    def is_full(self):
        return len(self.items) == self.capacity

    # print stack items from top to bottom
    def print_stack(self):
        print("Stack(top → bottom): ", list(reversed(self.items)))

    # clear the stack
    def clear(self):
        self.items = []
