"""
link: https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

1차 복습

❌ 네 코드에서 잘못된 핵심 4가지
❌ 1. result.next = final_number
여기서 정수(final_number) 를 next에 넣고 있음.
LinkedList의 node는 반드시 ListNode 객체여야 해.

즉:
result.next = ListNode(final_number)

이렇게 해야 링크가 연결된다.

❌ 2. pointer(result) 를 이동시키지 않음
너는 계속 result에만 덮어쓰기 하고 있어.
반드시 마지막에:
result = result.next
로 이동해야 한다.

❌ 3. l1 또는 l2가 없는 경우

else에서 l1.val = 0 이런 코드를 썼는데,
l1이 None이면 l1.val 접근 자체가 에러다.

그리고 없는 경우엔 0을 넣으려고 구조를 바꿀 필요가 없음.
None이면 그 자리는 0으로 취급하면 됨.

즉:

val1 = l1.val if l1 else 0
val2 = l2.val if l2 else 0


이렇게 해야 함.

❌ 4. while문 안에서 dummy head 접근을 완성하지 못함

dummy.node → result → result.next → …
이 흐름이 완성되어야 하는데 지금 result는 계속 처음 노드를 가리킴.

즉,

dummy는 “시작점(고정 포인터)”

result는 “현재 노드를 가리키며 앞으로 이동하는 포인터(작업용 포인터)”

이다.

요약:

dummy는 고정, result는 이동

이걸 분리해야 LinkedList를 만들 수 있어.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        
        dummy = ListNode(val=0)
        result = dummy
        while l1 is not None or l2 is not None or carry != 0:
            
            l1_val = l1.val if l1 else 0 
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry 
            carry = sum // 10
            final_val = sum % 10
            new_node = ListNode(final_val)
            result.next = new_node

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
            result = result.next
        return dummy.next
