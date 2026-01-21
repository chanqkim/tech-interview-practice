"""
link: https://leetcode.com/problems/repeated-substring-pattern/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching
"""


# time: O(n^2) space: O(1)
# time analysis: The outer loop runs for n/2 iterations, and the inner comparison takes O(n) time.
# Thus, the overall time complexity is O(n^2).
# space analysis: We use a constant amount of extra space for variables, so the space complexity is O(1).
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        str_len = len(s)

        for substr_len in range(1, str_len // 2 + 1):
            # if string length is over 1
            if str_len % substr_len != 0:
                continue

            substr = s[:substr_len]
            substr_cnt = str_len // substr_len
            print(f"substr:{substr}, cnt: {substr_cnt}")

            if substr * substr_cnt == s:
                return True
        return False
