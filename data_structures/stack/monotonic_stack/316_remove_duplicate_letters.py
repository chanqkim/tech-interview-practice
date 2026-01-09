"""
link: https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/remove-duplicate-letters/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-ii

similar questions: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/

# Important constraints:
# - Each character must appear exactly once
# - The relative order of characters must be preserved (not free sorting)
# - Result must be the smallest lexicographical sequence possible

"""

from collections import Counter


# time: O(n) space: O(n)
# Time Complexity: each character is processed at most twice (push and pop in stack)
# Space Complexity: legth of stack, visited set, and counter can go up to length of string
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count how many times each character appears in the string
        counter = Counter(s)

        stack = []  # Monotonic stack to build the result
        visited = set()  # Tracks characters already in the stack

        for char in s:
            # Decrease remaining count since we are processing this character
            counter[char] -= 1

            # If character is already used, skip it
            if char in visited:
                continue

            # Remove characters from stack if:
            # 1) The top character is lexicographically larger than current
            # 2) The top character will appear again later
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)

            # Add current character to stack and mark as visited
            stack.append(char)
            visited.add(char)

        # Convert stack to string
        return "".join(stack)
