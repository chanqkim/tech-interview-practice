"""
link: https://leetcode.com/problems/count-binary-substrings/description/
"""


# time: O(n) space: O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        current_len = 1
        previous_len = 0
        answer = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                answer += min(previous_len, current_len)
                previous_len = current_len
                current_len = 1

        answer += min(previous_len, current_len)
        return answer
