'''
link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/1996485806/?envType=problem-list-v2&envId=dsa-recursion-maze-recursion
Key Points:
1.Set up base cases for when one of the lists is empty
2.smaller node becomes the "head" of the merged list
3.head.next is set to the result of merging the remaining elements
4.return the merged head
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time: O(n + m) where n and m are the lengths of the two lists
# space: O(n + m) in the worst case when all nodes of one list are smaller than the other list, we will have to create a new list that contains all nodes of both
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Edge cases: if one of the lists is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1

        # Choose the smaller node and recurse
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        