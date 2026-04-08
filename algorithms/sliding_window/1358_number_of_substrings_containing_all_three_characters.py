'''
link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=problem-list-v2&envId=dsa-recursion-maze-sliding-window
'''

# time: O(n) space: O(1)
# time analysis: we traverse the string once with the right pointer, and the left pointer only moves forward → O(n)
# space analysis: we only use a fixed-size dictionary to track the last seen indices of 'a', 'b', and 'c' → O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        # [1] Track the last seen index of each character 'a', 'b', 'c'
        #     Initialized to -1 meaning "not seen yet"
        last_seen = {'a': -1, 'b': -1, 'c': -1}

        count = 0

        # [2] Iterate through every character with its index as the right pointer
        for right in range(len(s)):

            # [3] Update the last seen position of the current character
            last_seen[s[right]] = right

            # [4] If all three characters have been seen at least once
            #     (i.e., none of them is still -1)
            if -1 not in last_seen.values():

                # [5] The leftmost boundary of the current valid window
                #     = the smallest index among last seen positions
                #     Any left pointer from 0 to min(last_seen) forms a valid substring
                left = min(last_seen.values())

                # [6] All substrings starting from index 0..left and ending at 'right'
                #     are valid → add (left + 1) to count
                count += left + 1

        return count