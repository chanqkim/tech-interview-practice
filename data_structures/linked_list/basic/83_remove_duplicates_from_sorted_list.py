"""
link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1897601286/?envType=problem-list-v2&envId=dsa-association-slope-linked-list
Key Insight:
- Because the list is sorted, duplicates always appear consecutively.
- We only need to compare the current node with the next node.

Important Pitfall (What I got stuck on):
- When a duplicate node is removed, the pointer (cur) must NOT move.
- Moving the pointer immediately after deletion can skip nodes.
- Pointer movement must be conditional:
    - If duplicate → delete next node, stay on current
    - Else → move pointer forward
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointer to traverse the linked list
        cur = head

        # return head if list is empty
        if not head:
            return head

        # traverse the linked list until the end
        while cur and cur.next:
            # if current node value equals next node value, remove the duplicate
            if cur.val == cur.next.val:
                # delete next node by skipping it
                cur.next = cur.next.next
            else:
                # move forward only when values differ
                cur = cur.next

        return head
