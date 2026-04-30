'''
link: https://leetcode.com/problems/sum-of-scores-of-built-strings/description/?envType=problem-list-v2&envId=dsa-recursion-maze-rolling-hash
'''

# time: O(n) space: O(1)
# time analysis: O(n) to compute the rolling hashes and find the longest common prefix for each prefix
# space analysis: O(1) only a few variables for hashing and indices
# using Z-algorithm 
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)

        # Modulus to avoid overflow (large prime)
        MOD  = 10**9 + 7

        # Base for polynomial rolling hash
        BASE = 31

        # Hash from left → right (normal direction)
        forward_hash  = 0

        # Hash from right → left (simulated via power)
        backward_hash = 0

        # BASE^i term for backward hash
        power = 1

        total_score = 0

        # Iterate through the string
        for i in range(n):
            c = ord(s[i]) - ord('a') + 1

            forward_hash = (forward_hash * BASE + c) % MOD
            backward_hash = (backward_hash + c * power) % MOD
            power = (power * BASE) % MOD

            if forward_hash == backward_hash:
                total_score += i + 1

        return total_score % MOD