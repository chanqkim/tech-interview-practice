"""
Node Class
- needs value and pointer for the next node

LinkedList Class
- head: first node pointer

LinkedList functions:
append(value) → add new node to the end of the list
prepend(value) → add new node to the front of the list
find(value) → find and return the node that has the value(if value does not exist, return None)
delete(value) → delete node that has the value
print_list() → print linked_list

Advanced funtions
insert(index, value) → add value in the certain index of the LinkedList

reverse() → revers linked list

length() → return length of the list
"""


class Node:
    def __init__(self, value):
        self.next = None  # Pointer to the next node in the list (initially None)
        self.value = value  # Value stored in this node


class Linked_List:
    def __init__(self):
        self.head = None  # Head of the linked list, points to the first node

    # add new node at the end
    def append_value(self, value):
        current = self.head  # Start traversing from the head
        if self.head == None:  # If the list is empty
            self.head = Node(value)  # Create a new node and set it as head
        else:
            while current.next is not None:  # Traverse until the last node
                current = current.next  # Move to the next node
            current.next = Node(value)  # Append the new node at the end

    # add new node at the front
    def prepend_value(self, value):
        new_node = Node(value)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update head to point to the new node

    def find_value(self, value):
        if self.head is None:  # If the list is empty
            return None  # Value cannot be found
        else:
            current = self.head  # Start traversing from the head
            while current is not None:
                if current.value == value:  # Check if current node has the target value
                    return current  # Return the node if found
                else:
                    current = current.next  # Move to the next node

    def delete_value(self, value):
        if self.head is None:  # If the list is empty
            return None  # Nothing to delete
        else:
            current = self.head  # Start traversing from head
            # if deleted element is the first element
            if self.head is not None and self.head.value == value:
                self.head = (
                    self.head.next
                )  # Remove head by updating it to the next node
            while current.next is not None:
                if current.next.value == value:  # Check if next node is the target
                    current.next = (
                        current.next.next
                    )  # Skip the next node, effectively deleting it
                else:
                    current = current.next  # Move to the next node

    def print_list(self):
        ret = []  # List to collect node values
        current = self.head  # Start from the head
        if current is None:  # If list is empty
            return ret  # Return empty list

        while current is not None:  # Traverse all nodes
            ret.append(current.value)  # Add current node's value to the list
            current = current.next  # Move to the next node
        return ret  # Return the collected values

    def insert_value(self, index, value):
        current = self.head  # Start from head
        new_node = Node(value)  # Create a new node with the value

        if current is None or index == 0:  # If list is empty or inserting at head
            new_node.next = self.head  # Link new node to current head
            self.head = new_node  # Update head to the new node

        else:
            current_index = 0  # Initialize index counter
            current = self.head  # Start traversing from head
            while current is not None:
                if current_index == index - 1:  # Stop at node just before target index
                    new_node.next = current.next  # Link new node to next node
                    current.next = new_node  # Link current node to new node
                    break  # Insertion done, exit loop
                current = current.next  # Move to the next node
                current_index += 1  # Increment index counter

    def reverse_list(self):
        current = self.head

        # if node is one, return linked_list
        if current.next is None:
            return

        # prev: previous node pointer, current: current node pointer, next_temp: next node pointer
        prev = None

        while current.next is not None:
            next_temp = current.next  # store next node
            current.next = prev  # reverse the pointer
            prev = current  # move prev to current
            current = next_temp  # move current to next node

    # return length of linked list
    def list_length(self):
        current = self.head
        list_length = 0

        # traverse linked list and count nodes
        while current is not None:
            list_length += 1
            current = current.next

        return list_length
