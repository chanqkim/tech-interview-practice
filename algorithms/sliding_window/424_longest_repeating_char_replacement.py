'''
link: https://leetcode.com/problems/longest-repeating-character-replacement/?envType=problem-list-v2&envId=dsa-recursion-maze-sliding-window
'''

# time: O(n)
# space: O(1) only 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # save the frequency of each character in the current window
        count = {}

        # sliding window left pointer
        left = 0

        # most frequent character count in the current window
        # (key point: the rest will be changed based on this value)
        max_freq = 0

        # the length of the longest valid window found (answer)
        result = 0

        # expand the window by moving the right pointer
        for right in range(len(s)):

            # include the current character in the window and increase its frequency
            count[s[right]] = count.get(s[right], 0) + 1

            # update the most frequent character count in the current window
            # (key point: the rest will be changed based on this value)
            max_freq = max(max_freq, count[s[right]])

            # current window length
            # = (right - left + 1)

            # number of characters to replace =
            # window length - most frequent character count
            # if this value is greater than k, then this window is invalid
            while (right - left + 1) - max_freq > k:

                # remove the leftmost character (shrink the window)
                count[s[left]] -= 1

                # move the left pointer
                left += 1

            # current window is always "valid"
            # update the maximum length
            result = max(result, right - left + 1)

        return result