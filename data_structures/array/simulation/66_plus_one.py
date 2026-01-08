"""
link: https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/plus-one/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-i
"""

from typing import List


# Time Complexity: O(n)
# - In the worst case, we traverse the entire array once (when all digits are 9).
# Space Complexity: O(1)
# - The operation is done in-place.
# - Only in the edge case (all digits are 9) do we allocate a new array of size n+1.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the digits from right to left
        # This allows us to correctly handle carry propagation
        for i in range(len(digits) - 1, -1, -1):
            # Case 1: current digit is less than 9
            # We can safely add 1 without carry
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No further processing needed

            # Case 2: current digit is 9
            # Adding 1 causes carry, so set this digit to 0
            digits[i] = 0

        # If we exit the loop, all digits were 9 (e.g., [9, 9, 9])
        # The result becomes [1, 0, 0, 0]
        return [1] + digits
