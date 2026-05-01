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

# using rolling hash + binary search
# time: O(n log n) space: O(n)
# time analysis: O(n) to compute the rolling hashes + O(n log n) for each prefix, we do a binary search to find the longest common prefix → O(n log n)
# space analysis: O(n) for the hash and power arrays
class Solution2:
    def sumScores(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        base = 31
        
        # hash and power arrays for rolling hash
        h = [0] * (n + 1)
        p = [1] * (n + 1)

        # looop to compute the rolling hash values and powers of the base
        for i in range(n):
            h[i+1] = (h[i] * base + (ord(s[i]) - ord('a') + 1)) % mod
            p[i+1] = (p[i] * base) % mod

        # return the hash of the substring s[l:r] using the precomputed hash and power arrays   
        def get_hash(l, r): 
            return (h[r] - h[l] * p[r-l]) % mod
        
        total_score = 0
        for i in range(n):
            # use binary search to find LCP length between prefix s[0:i] and suffix s[i:n]
            low, high = 1, n - i
            lcp = 0
            while low <= high:
                mid = (low + high) // 2
                # compare the hash of the prefix s[0:mid] with the hash of the suffix s[i:i+mid]
                if get_hash(0, mid) == get_hash(i, i + mid):
                    lcp = mid
                    low = mid + 1
                else:
                    high = mid - 1
            total_score += lcp
            
        return total_score