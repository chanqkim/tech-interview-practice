"""
link: https://leetcode.com/problems/repeated-string-match/submissions/1894141742/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching
tips:
limit the number of repetition to len(a) < len(b)
add one more repetition to cover edge cases
"""


# time: O(n^2) space: O(n)
# Time Complexity: O(n^2) in the worst case due to repeated string concatenation and substring checks.
# Space Complexity: O(n) for storing the repeated string.
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Initialize variables
        repeated_a = a
        # number of times a is repeated
        count = 1

        # append a to repeated_a until its length is at least that of b
        while len(repeated_a) < len(b):
            repeated_a += a
            count += 1

        # Check if b is now a substring of repeated_a
        if b in repeated_a:
            return count

        # Check one more repetition to cover edge cases
        repeated_a += a
        count += 1
        if b in repeated_a:
            return count

        return -1
