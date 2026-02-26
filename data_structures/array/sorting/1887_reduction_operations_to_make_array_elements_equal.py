"""
link: https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/submissions/1931747686/?envType=problem-list-v2&envId=dsa-sorting-plateau-sorting
"""

from typing import List


# time: O(n log n) space: O(1)
# time analysis: sorting the array takes O(n log n), and a single pass to count
# the operations takes O(n), resulting in an overall time complexity of O(n log n).
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # sort the array in ascending order to group identical values together
        nums.sort()

        # initialize total operations and the number of steps to reach the current value
        total_ops = 0
        up_steps = 0  # number of steps to reach the current value

        # loop through the array and increment steps whenever the value changes
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up_steps += 1
            # keep adding how many steps the current number is above the minimum (up_steps)
            total_ops += up_steps

        return total_ops
