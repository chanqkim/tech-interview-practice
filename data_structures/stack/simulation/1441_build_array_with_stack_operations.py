"""
link: https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
"""

from typing import List


# time: O(n) space: O(n)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        current_number = 1
        target_index = 0
        while target_index < len(target):
            # push current number to stack
            answer.append("Push")

            # if current number is in target, move to next target index
            if current_number == target[target_index]:
                target_index += 1

            # if current number is not in target, pop it from stack
            else:
                answer.append("Pop")
            current_number += 1

        return answer
