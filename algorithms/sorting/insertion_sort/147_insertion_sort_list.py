"""
link: https://leetcode.com/problems/insertion-sort-list/?envType=problem-list-v2&envId=dsa-sorting-plateau-counting-sort-merge-sort-quickselect
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time: O(n^2) space: O(1)
# time analysis: In the worst case (when the list is sorted in reverse order), each node will be compared with all the previously sorted nodes, leading to O(n^2) time complexity
# space analysis: The algorithm uses only a constant amount of extra space for pointers and temporary variables, resulting in O(1) space complexity.
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node helps handle insertion at the head easily
        dummy = ListNode(0)

        # current pointer traverses the original list
        curr = head

        # iterate through each node in the original list
        while curr:
            # store next node before modifying pointers
            next_node = curr.next

            # find the correct position in the sorted part
            prev = dummy

            # move prev until the correct insertion point is found
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # insert current node between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # move to next node in the original list
            curr = next_node

        # return the head of the sorted list
        return dummy.next
