"""
link: https://leetcode.com/problems/concatenation-of-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
"""

# solution1 time: O(n) space: O(n)
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# solution2: index based approach, time: O(n) space: O(n)
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_len = len(nums)
        answer = [0] * (2 * list_len)
        for i in range(len(nums)):
            answer[i] = nums[i]
            answer[list_len + i] = nums[i]
        return answer
