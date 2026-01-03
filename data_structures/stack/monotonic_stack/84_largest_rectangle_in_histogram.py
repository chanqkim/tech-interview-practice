"""
link: https://leetcode.com/problems/largest-rectangle-in-histogram/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack
"""

from typing import List


# time: O(n) space: O(n)
# Time complexity: O(n) because each index is pushed and popped at most once.
# Space complexity: O(n) due to the auxiliary stack.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack to store indices of histogram bars
        stack = []

        # Variable to keep track of the maximum area found
        max_area = 0

        for i in range(len(heights) + 1):
            # Use 0 height for the imaginary bar at the end
            current_height = heights[i] if i < len(heights) else 0

            # While there is a previous bar in the stack and the current bar is shorter
            while stack and heights[stack[-1]] > current_height:
                prev_index = stack.pop()  # Get the index of the taller bar
                height = heights[prev_index]  # Height of the popped bar

                # Width calculation:
                # if popped bar exists in stack
                if stack:
                    # left boundary: stack[-1] + 1
                    # right boundary: i - 1
                    width = i - stack[-1] - 1
                # If stack is empty, it means the popped bar was the smallest so far
                # So width is from start (0) to current index (i)
                else:
                    width = i

                # Calculate area with popped bar as the smallest height
                area = height * width
                # Update max area if needed
                max_area = max(max_area, area)
            # Push current index onto stack
            stack.append(i)

        # Return the maximum area found
        return max_area
