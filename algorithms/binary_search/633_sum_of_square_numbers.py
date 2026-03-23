'''
link: https://leetcode.com/problems/sum-of-square-numbers/?envType=problem-list-v2&envId=dsa-sorting-plateau-binary-search
'''

import math

# solution 1: using binary search
# time: O(sqrt(c) * log(sqrt(c))) space: O(1)
# time analysis: iterating through possible values of a takes O(sqrt(c)) time, and for each a, performing a binary search to check if b^2 is a perfect square takes O(log(sqrt(c))) time → O(sqrt(c) * log(sqrt(c)))
# space analysis: using only a constant amount of extra space → O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # loop a from 0 to sqrt(c)
        # a^2 <= c, so the maximum value of a is sqrt(c)
        for a in range(int(math.sqrt(c)) + 1):

            # b^2 should satisfy b^2 = c - a^2
            b2 = c - a * a

            # range of b's possible values: 0 ~ sqrt(c)
            left, right = 0, int(math.sqrt(c))

            # start binary search
            while left <= right:

                # calculate the middle value of b
                mid = (left + right) // 2

                # calculate mid^2 
                if mid * mid == b2:
                    # exact match found → a^2 + b^2 = c → return True
                    return True

                # if mid^2 is less than b^2, we need a larger value for b
                elif mid * mid < b2:
                    left = mid + 1

                # if mid^2 is greater than b^2, we need a smaller value for b
                else:
                    right = mid - 1

        # if no value satisfies a^2 + b^2 = c, return False
        return False