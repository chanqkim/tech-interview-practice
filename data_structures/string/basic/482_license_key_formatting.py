"""
link: https://leetcode.com/problems/license-key-formatting/?envType=problem-list-v2&envId=dsa-sequence-valley-string

Problem Insight:
- Reformat a license key string so that:
  1) All letters are uppercase
  2) Groups are of length k, except possibly the first group
  3) Groups are separated by '-'
- Backward processing is easier because the last group is always length k

Key Points:
- Remove existing '-' characters
- Convert all letters to uppercase
- Build groups from the end to handle variable first group length
- Reverse the final list and join with '-' to get the result
"""


# time: O(n) space: O(n)
# Time: iterate through string twice → O(n)
# Space: The result list stores all characters. Slicing creates temporary substrings.
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 1. Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()

        # 2. Split into groups of size k from the end
        result = []
        while len(s) > k:
            result.append(s[-k:])
            s = s[:-k]
        result.append(s)

        # 3. Join the groups with dashes
        return "-".join(result[::-1])
