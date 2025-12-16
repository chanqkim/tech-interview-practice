"""
Link: https://leetcode.com/problems/palindrome-number/description/
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


# Revsersing number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        origin_number = x
        reversed_number = 0

        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10
        # return True if origin_number equals reversed_number
        return origin_number == reversed_number

    # using stack
    def isPalindromeUsingStack(self, x: int) -> bool:
        if x < 0:
            return False

        origin_number = x
        # create Stack
        stack = []
        while x > 0:
            stack.append(x % 10)
            x //= 10

        # compare stack with number
        while stack:
            last_number = stack.pop()
            print(last_number)
            if last_number != origin_number % 10:
                return False
            origin_number = origin_number // 10
        return True


print(Solution().isPalindrome(121))
print(Solution().isPalindromeUsingStack(12321))
