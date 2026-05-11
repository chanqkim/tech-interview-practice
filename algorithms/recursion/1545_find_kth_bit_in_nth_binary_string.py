'''
link: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=problem-list-v2&envId=dsa-recursion-maze-recursion
'''

# time: O(n) space: O(n)
# time analysis: O(n) to build the nth binary string, which has length 2^n - 1
# space analysis: O(n) for the recursion stack and the strings built during the recursion
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        # helper function to recursively build the nth binary string and find the kth bit
        def helper(n, k):
            
            # base case: the 1st binary string is "0"
            if n == 1:
                return "0"

            # the length of the nth binary string is 2^n - 1
            length = (1 << n) - 1
            # the middle index of the nth binary string (1-based index)
            mid = length // 2 + 1

            # if k is the middle index, return "1"
            if k == mid:
                return "1"

            # if k is in the left half, it is the same as the kth bit in the (n-1)th binary string
            elif k < mid:
                return helper(n - 1, k)

            # if k is in the right half, it is the inverse of the (mirror)th bit in the (n-1)th binary string
            else:
                # the mirror index in the (n-1)th binary string for the right half
                mirror = length - k + 1
                # get the bit at the mirror index in the (n-1)th binary string
                bit = helper(n - 1, mirror)

                # return the inverse of the bit (if bit is "0", return "1"; if bit is "1", return "0")
                return "1" if bit == "0" else "0"

        return helper(n, k)