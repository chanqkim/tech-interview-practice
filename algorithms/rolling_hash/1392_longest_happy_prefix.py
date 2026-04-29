'''
link: https://leetcode.com/problems/longest-happy-prefix/?envType=problem-list-v2&envId=dsa-recursion-maze-rolling-hash
'''

# time: O(n) space: O(1)
# time analysis: O(n) to compute the rolling hashes and find the longest happy prefix
# space analysis: O(1) only a few variables for hashing and indices
class Solution:
    def longestPrefix(self, s: str) -> str:
        # length of the input string
        n = len(s)
       
       # Modulus to avoid overflow (large prime)
        MOD  = 10**9 + 7

        # Base for polynomial rolling hash
        BASE = 31

        # Hash from left → right (normal direction)
        prefix_hash = 0
        
        # Hash from right → left (simulated via power)
        suffix_hash = 0
        
        power = 1
        best = 0  # longest happy prefix length found so far

        # loop through the string to compute rolling hashes and compare (not including the full string)
        for i in range(n - 1): 
            # prefix: s[0..i], suffix: s[n-1-i..n-1]
            c_left  = ord(s[i])         - ord('a') + 1  
            c_right = ord(s[n - 1 - i]) - ord('a') + 1  

            # prefix: from left to right (normal direction)
            prefix_hash = (prefix_hash * BASE + c_left)  % MOD
            # suffix: from right to left (simulated via power)
            suffix_hash = (suffix_hash + c_right * power) % MOD
            power       = (power * BASE)                  % MOD

            # If hashes match → prefix [0..i] == suffix [n-1-i..n-1] (probabilistically)
            if prefix_hash == suffix_hash:
                # update longest happy prefix length
                best = i + 1  
        return s[:best]