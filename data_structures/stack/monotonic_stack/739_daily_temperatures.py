"""
link: https://leetcode.com/problems/daily-temperatures/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack
"""

from typing import List


# time: O(n) space: O(n)
# Time complexity: O(n) because each index is pushed and popped at most once.
# Space complexity: O(n) due to the auxiliary stack and the output list.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Monotonic stack to store indices of temperatures
        answer = (
            [0] * len(temperatures)
        )  # Initialize answer list with zeros because days without a warmer future temperature should remain 0 by default.

        for i in range(len(temperatures)):
            # While there is a previous day in the stack and the current temperature is warmer than that day's temperature
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()  # Get the index of the colder day
                answer[prev_index] = (
                    i - prev_index
                )  # Calculate days(index gap) until warmer temperature

            stack.append(i)  # Push current day's index onto stack

        return answer  # Return the list of days until a warmer temperature
