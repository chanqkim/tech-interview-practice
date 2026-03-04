"""
link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1937725455/?envType=problem-list-v2&envId=dsa-sorting-plateau-counting-sort-merge-sort-quickselect
"""

import heapq
from typing import List


# time: O(n log k) space: O(k)
# time analysis: iterating through the array takes O(n), and each insertion into the heap takes O(log k) time, resulting in an overall time complexity of O(n log k).
# space analysis: the heap will contain at most k elements at any time, so the space complexity is O(k).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap to keep track of the k largest elements
        min_heap = []

        for num in nums:
            # add the current number to the heap
            heapq.heappush(min_heap, num)

            # if the heap exceeds size k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # the root of the heap is the kth largest element
        return min_heap[0]
