"""
link: https://leetcode.com/problems/detect-capital/?envType=problem-list-v2&envId=dsa-sequence-valley-string
"""

# time: O(n) space: O(1)
# Time: check string length — O(n)
# space: O(1) — no additional memory used


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all letters are uppercase or lowercase
        if word.isupper() or word.islower():
            return True
        # Check if only the first letter is uppercase
        if word[0].isupper() and word[1:].islower():
            return True
        return False
