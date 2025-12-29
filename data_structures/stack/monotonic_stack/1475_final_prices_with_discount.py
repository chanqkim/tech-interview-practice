"""
link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack
"""

from typing import List


# time: O(n) space: O(n)
# Time complexity: because each index is pushed and popped at most once.
# Space complexity: O(n) due to the auxiliary stack.
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Stack will store indices of items waiting for a discount
        stack = []

        # Copy original prices to apply discounts in-place
        answer = prices[:]

        # Iterate through each price from left to right
        for i in range(len(prices)):
            # While there is a previous item in the stack
            # AND the current price can act as a discount
            # (current price <= previous price)
            while stack and prices[stack[-1]] >= prices[i]:
                # Get the index of the item receiving the discount
                prev_index = stack.pop()

                # Apply discount using the first smaller-or-equal price to the right
                answer[prev_index] = prices[prev_index] - prices[i]

            # Push current index onto stack
            # It may receive a discount from a future price
            stack.append(i)

        # Return final prices after all discounts applied
        return answer
