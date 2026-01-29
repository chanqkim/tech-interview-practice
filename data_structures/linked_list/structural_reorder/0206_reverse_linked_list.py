"""
link: https://leetcode.com/problems/reverse-linked-list/submissions/1900589216/?envType=problem-list-v2&envId=dsa-association-slope-linked-list
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time: O(n) space: O(1)
# time analysis: traversing the entire linked list once → O(n)
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointers for previous and current nodes
        prev = None
        curr = head

        # traverse the linked list and reverse the pointers
        while curr:
            # store next node
            next_node = curr.next
            # reverse the pointer
            curr.next = prev
            # move previous pointer forward
            prev = curr
            # move pointers forward
            curr = next_node
        return prev
