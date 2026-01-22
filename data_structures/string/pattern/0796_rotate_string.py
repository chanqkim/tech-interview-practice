"""
link: https://leetcode.com/problems/rotate-string/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching

# checklist
1. do string needs to be "moved" one by one?
- or can it be converted to a whole set?
2. can all results fit in one big string?
- if YES -> s + s
3. is the final check just "inclusion"?
- goal in s+s
"""


# Brute force solution
# time: O(n^2) space: O(1)
# time analysis: The outer loop runs for n/2 iterations, and the inner comparison takes
# O(n) time. Thus, the overall time complexity is O(n^2).
# space analysis: We use a constant amount of extra space for variables, so the space complexity is O(1).
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return False if lengths are different
        if len(s) != len(goal):
            return False

        # count of rotations
        cnt = len(s)

        # loop for each rotation
        while cnt > 0:
            # rotate string by 1
            s = s[-1] + s[:-1]
            if s == goal:
                return True
            # decrease rotation count
            cnt -= 1
        # if no rotation matches goal, return False
        return False


# Optimal solution
# time: O(n) space: O(n)
# time analysis: The string concatenation and substring search operations can be performed in linear time using
# efficient string matching algorithms, leading to an overall time complexity of O(n).
# space analysis: The space complexity is O(n) due to the storage of the concatenated
class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        # if lengths differ, cannot be rotations
        if len(s) != len(goal):
            return False

        # concatenate s with itself
        ss = s + s

        # check if goal is a substring of ss
        return goal in ss
