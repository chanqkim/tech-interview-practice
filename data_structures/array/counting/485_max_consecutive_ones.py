"""
link: https://leetcode.com/problems/max-consecutive-ones/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
"""

from typing import List


# solution1: O(n) space: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_count = 0
        current_consecutive_count = 0

        for i in nums:
            if i == 1:
                current_consecutive_count += 1
                max_consecutive_count = max(
                    max_consecutive_count, current_consecutive_count
                )
            else:
                current_consecutive_count = 0
        return max_consecutive_count
