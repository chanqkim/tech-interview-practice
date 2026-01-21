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


# Optimal solution
# time: O(n) space: O(n)
# time analysis: The string concatenation and substring search operations can be performed in linear time using
# efficient string matching algorithms, leading to an overall time complexity of O(n).
# space analysis: The space complexity is O(n) due to the storage of the concatenated
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # create a new string by concatenating s with itself and removing the first and last characters to avoid original string match
        ss = (s + s)[1:-1]
        return s in ss
