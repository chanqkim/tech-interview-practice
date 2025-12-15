"""
link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
"""

from typing import List


# brute force: time: O(n) space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_num = len(nums)
        full_set = set([i for i in range(1, max_num + 1)])
        return list(full_set - set(nums))


# optimal: time: O(n) space: O(1)
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: mark existing numbers
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Step 2: collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
