"""
link: https://leetcode.com/problems/odd-even-linked-list/description/?envType=problem-list-v2&envId=dsa-association-slope-linked-list

Important Pitfall (What I got stuck on):
separate odd and even pointers
→ rearrange each pointer's next
→ connect the end of odd list to the head of even list
1 → 2 → 3 → 4 → 5
↓   ↓   ↓
odd    odd     odd
    even even
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # pointers for odd and even nodes
        odd = head
        even = head.next
        even_head = even

        # loop until the end of the list
        while even and even.next:
            # connect odd nodes with even nodes
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        # connect the end of odd list to the head of even list
        odd.next = even_head
        return head
