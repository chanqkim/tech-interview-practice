"""
link: https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
"""

from typing import List


# time: O(n) space: O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        nums_set = set()
        dup_number = 0

        # use set to find duplicate number
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                dup_number = i

        # calculate missing number using sum formula
        correct_sum = len_nums * (len_nums + 1) / 2
        current_sum = sum(nums)
        missing_no = int(correct_sum - (current_sum - dup_number))

        return [dup_number, missing_no]


# time: O(n) space: O(1)
class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        # place each number at its correct index (v -> index v-1)
        while i < n:
            correct_idx = nums[i] - 1
            # if current is not at correct position and not a duplicate at target, swap
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # after placement, the place where nums[i] != i+1 reveals duplicate/missing
        for idx in range(n):
            if nums[idx] != idx + 1:
                return [nums[idx], idx + 1]

        # problem constraints guarantee there is always one duplicate/missing
        return [-1, -1]
