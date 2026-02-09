"""
link: https://leetcode.com/problems/make-sum-divisible-by-p/submissions/1913530916/?envType=problem-list-v2&envId=dsa-association-slope-prefix-sum
"""

from typing import List


# time: O(n) space: O(n)
# time analysis: traversing the entire list once → O(n)
# space analysis: storing prefix sums in a hash map → O(n)
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # calculate the total sum and its remainder when divided by p
        total = sum(nums)
        rem = total % p

        # if the total sum is already divisible by p, return 0
        if rem == 0:
            return 0

        # initialize prefix sum, seen map, and result
        prefix = 0
        seen = {0: -1}
        res = len(nums)

        # loop through the array to find the minimum subarray
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem) % p
            if target in seen:
                res = min(res, i - seen[target])
            seen[prefix] = i

        return res if res < len(nums) else -1
