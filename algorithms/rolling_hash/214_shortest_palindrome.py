'''
link: https://leetcode.com/problems/shortest-palindrome/description/?envType=problem-list-v2&envId=dsa-recursion-maze-rolling-hash
'''

# time: O(n) space: O(1)
# time analysis: O(n) to compute the rolling hashes and find the longest palindromic prefix
# space analysis: O(1) only a few variables for hashing and indices
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        # Edge case: if string is empty == a palindrome
        if n == 0:
            return s

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

        # Length of the longest palindromic prefix found so far
        best  = 0

        # Iterate through the string
        for i in range(n):

            # Map character to integer (a=1, b=2, ..., z=26)
            c = ord(s[i]) - ord('a') + 1

            # Update forward hash:
            # shift previous hash and add current character
            forward_hash = (forward_hash * BASE + c) % MOD

            # Update backward hash:
            # add current character weighted by BASE^i
            backward_hash = (backward_hash + c * power) % MOD

            # Update power for next iteration (BASE^(i+1))
            power = (power * BASE) % MOD

            # If hashes match → prefix [0..i] is palindrome (probabilistically)
            if forward_hash == backward_hash:
                best = i + 1  # update longest palindromic prefix length

        # Take the non-palindromic suffix
        # Reverse it and prepend to original string
        return s[best:][::-1] + s