"""
link: https://leetcode.com/problems/rotate-string/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching
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
