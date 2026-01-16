"""
link: https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/?source=submission-ac

Category:
- Heap
- Greedy (Reverse Simulation)

Key Idea:
- Reverse the process using max heap
- Always reduce the largest element
- Use modulo to skip repeated subtraction
"""

import heapq
from typing import List


# time: O(n log n) space: O(n)
# time analysis: n log n for each heap operation, n is the value of the largest element
# space analysis: O(n) for the heap
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # - value to use min-heap as max-heap
        heap = [-x for x in target]
        heapq.heapify(heap)

        total = sum(target)

        while True:
            # pop the largest value
            largest = -heapq.heappop(heap)

            # calculate the rest sum
            rest = total - largest

            # if largest or rest is 1, we can always form the target
            if largest == 1 or rest == 1:
                return True

            # if rest is 0 or largest <= rest, it's impossible
            if rest == 0 or largest <= rest:
                return False

            # calculate the previous value before largest was added
            prev = largest % rest

            # if prev is 0, the only valid previous value is rest
            if prev == 0:
                prev = rest

            # if prev is still less than 1, it's a failure
            if prev < 1:
                return False

            # update the heap and total
            heapq.heappush(heap, -prev)
            total = rest + prev
