"""
link: https://leetcode.com/problems/last-stone-weight/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

Key Notes (For Review & Interviews)

1. Why Heap?
- The problem repeatedly requires selecting the two largest elements
- Heap (priority queue) is optimal for repeated max/min extraction
- Sorting every time would be inefficient (O(n log n) per iteration)

2. Why Negative Values?
- Python heapq only provides a min-heap
- By inserting negative values, we simulate a max-heap
- The most negative value corresponds to the largest original value
"""

import heapq
from typing import List

# Time Complexity: O(n log n)
# - Building the heap with heapify takes O(n)
# - Each pop and push operation takes O(log n)
# - In the worst case, we perform pop/push operations up to n times
# - Therefore, overall time complexity is O(n log n)


# Space Complexity: O(n)
# - The heap stores up to n elements
# - Additional space usage is constant
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use negative values to simulate max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # loop until one or no stones left
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # heaviest stone
            x = -heapq.heappop(max_heap)  # second heaviest stone

            # if they are not equal, push the difference back
            # if y == x, both stones are destroyed(do nothing)
            if y > x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0
