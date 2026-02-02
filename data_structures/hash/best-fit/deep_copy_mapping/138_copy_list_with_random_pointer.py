"""
link: https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=dsa-association-slope-hash

Key Idea:
This is NOT a simple linked list traversal problem.
Hash map is required to preserve reference relationships
between original nodes and copied nodes.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, val: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = val
        self.next = next
        self.random = random


# time: O(n) space: O(n)
# time analysis: traversing the entire linked list once → O(n)
# space analysis: storing nodes in a hash map → O(n)
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Hash map to store the mapping from original nodes to their copies
        hash = {}

        # First pass: create copies of all nodes and store them in the hash map
        current = head
        while current:
            hash[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers for the copied nodes
        current = head
        while current:
            if current.next:
                hash[current].next = hash[current.next]
            if current.random:
                hash[current].random = hash[current.random]
            current = current.next

        # Return the head of the copied linked list
        return hash[head]
