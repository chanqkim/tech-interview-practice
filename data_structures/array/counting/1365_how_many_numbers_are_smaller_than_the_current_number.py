"""
link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
"""

from typing import List


# brute force solution time: O(n^2) space: O(1)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            small_num_cnt = 0
            for j in nums:
                if i > j:
                    small_num_cnt += 1
            answer.append(small_num_cnt)
        return answer


# optimal solution using counting sort time: O(n) space: O(1)
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101  # since the constraints say 0 <= nums[i] <= 100

        # count occurrences of each number
        for num in nums:
            count[num] += 1

        # modify count array to have the count of numbers less than or equal to index
        for i in range(1, 101):
            count[i] += count[i - 1]

        # build the answer array
        answer = []
        for num in nums:
            if num == 0:
                answer.append(0)
            else:
                answer.append(count[num - 1])  # numbers smaller than current number

        return answer


# sorting based solution time: O(n log n) space: O(n)
class Solution3:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        rank = {}
        for idx, val in enumerate(sorted_nums):
            # only set the rank for the first occurrence to handle duplicates
            if val not in rank:
                rank[val] = idx

        return [rank[x] for x in nums]
