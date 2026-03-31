'''
link: https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=dsa-recursion-maze-two-pointers
'''

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# time: O(n) space: O(1)
# time analysis: in the worst case, we traverse all nodes once → O(n)
# space analysis: using only a constant amount of extra space for the two pointers → O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # start two pointers at the head of the linked list
        slow = head
        fast = head
        
        # Iterate util fast and fast.next is not None = reached the end of the linked list
        while fast is not None and fast.next is not None:
            
            # move two poin ters at different speeds: slow moves one step, fast moves two steps
            slow = slow.next        
            fast = fast.next.next  
            
            # if twop pointer meets == cycle exits 
            if slow == fast:
                return True
        
        # if list is iterated(fast.next is None), there is no cycle
        return False