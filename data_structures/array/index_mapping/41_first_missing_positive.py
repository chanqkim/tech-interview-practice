"""
link: https://leetcode.com/problems/first-missing-positive/submissions/1906661099/?envType=problem-list-v2&envId=dsa-association-slope-hash
"""

from typing import List


# time: O(n) space: O(1)
# time analysis: traversing the entire list a constant number of times → O(n)
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        hash = set()

        # save only 1 to n values in the hash set
        for x in nums:
            if 1 <= x <= n:
                hash.add(x)

        # loop through 1 to n to find the first missing positive
        for i in range(1, n + 1):
            if i not in hash:
                return i

        # if all are present, return n+1
        return n + 1
