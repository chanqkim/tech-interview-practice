"""
leetcode: https://leetcode.com/problems/two-sum/submissions/1902972489/?envType=problem-list-v2&envId=dsa-association-slope-hash
Why:
- No choice branching
- Single pass
- Store seen values and lookup complement
"""

from typing import List


# time: O(n) space: O(n)
# time analysis: traversing the entire list once → O(n)
# space analysis: storing elements in a hash map → O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()

        # traverse the list
        for i in range(len(nums)):
            # check if complement exists in hash
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            # store the number with its index in hash
            else:
                hash[nums[i]] = i
