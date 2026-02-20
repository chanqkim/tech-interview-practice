"""
link: https://leetcode.com/problems/ways-to-make-a-fair-array/submissions/1925030651/?envType=problem-list-v2&envId=dsa-association-slope-prefix-sum
"""

from typing import List


# Time Complexity: O(n)
# - One pass to compute total even/odd sums
# - One pass to evaluate each removal
# Space Complexity: O(1)
# - Only constant extra variables are used (no prefix arrays stored)
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Step 1: compute total sum of even-indexed and odd-indexed elements
        total_even = sum(nums[i] for i in range(0, len(nums), 2))
        total_odd = sum(nums[i] for i in range(1, len(nums), 2))

        # prefix sums for the left side of the current index
        left_even = 0
        left_odd = 0

        result = 0

        # Step 2: iterate through each index as a candidate for removal
        for i, num in enumerate(nums):
            # Remove current element from total sums (treat as right side)
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num

            # After removing index i:
            # right side parity flips
            # new_even = left_even + total_odd
            # new_odd  = left_odd  + total_even
            if left_even + total_odd == left_odd + total_even:
                result += 1

            # Update left prefix sums for next iteration
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return result
