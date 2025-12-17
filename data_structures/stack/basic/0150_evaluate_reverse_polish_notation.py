"""
link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
"""

from typing import List


# time: O(n) space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # iterate through each token
        for i in tokens:
            # check if token is a number or an operator
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))

            # if token is an operator, pop two numbers from stack and perform the operation
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == "+":
                    calc_num = num2 + num1
                elif i == "-":
                    calc_num = num2 - num1
                elif i == "*":
                    calc_num = num2 * num1
                else:
                    calc_num = int(num2 / num1)
                # push the result back to stack
                stack.append(calc_num)

        return stack[0]
