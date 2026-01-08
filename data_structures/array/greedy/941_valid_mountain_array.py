"""
link:
https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/valid-mountain-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-i

Problem Insight:
- A valid mountain array must satisfy all of the following:
  1) The sequence strictly increases
  2) It reaches exactly one peak (the peak cannot be the first or last element)
  3) The sequence strictly decreases after the peak
- The array must be traversed in a single direction without backtracking
- No additional data structures (stack, queue) are required

Key Idea:
- Use a single pointer to scan the array
- Phase 1: move upward while the sequence is strictly increasing
- Phase 2: move downward while the sequence is strictly decreasing
- If the pointer reaches the last index exactly, the array is a valid mountain
"""

from typing import List


# One-pass greedy approach
# Time Complexity: O(n)
# - The array is traversed only once
# Space Complexity: O(1)
# - No additional data structures are used
# - Only a pointer and a few variables are maintained
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        len_array = len(arr)

        # A mountain array must contain at least three elements
        if len_array < 3:
            return False

        # Pointer used to traverse the array
        pointer = 0

        # Phase 1: strictly increasing sequence
        # Move the pointer forward while the next element is larger
        while pointer < len_array - 1 and arr[pointer] < arr[pointer + 1]:
            pointer += 1

        # The peak cannot be at the beginning or at the end of the array
        if pointer == 0 or pointer == len_array - 1:
            return False

        # Phase 2: strictly decreasing sequence
        # Continue moving the pointer forward while the next element is smaller
        while pointer < len_array - 1 and arr[pointer] > arr[pointer + 1]:
            pointer += 1

        # If the pointer reaches the last index,
        # the array strictly increased and then strictly decreased
        return pointer == len_array - 1
