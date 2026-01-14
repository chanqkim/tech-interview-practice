"""
link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

When a problem asks for the k smallest results from a large,
ordered combination space,
use a min-heap with (cost, state) and expand neighbors lazily.
"""

import heapq
from typing import List

# time: O(k log k) space: O(k)


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # return empty list if any input list is empty or k is 0
        if not nums1 or not nums2 or k == 0:
            return []

        answer = []
        heap = []
        # set to avoid duplicate pairs
        dup_set = set()

        # add first pair in heap
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        # add first pair in dup set
        dup_set.add((0, 0))

        while heap and len(answer) < k:
            # pop and get smallest sum pair
            _, i, j = heapq.heappop(heap)
            answer.append([nums1[i], nums2[j]])

            # add i+1, j value set
            if i + 1 < len(nums1) and (i + 1, j) not in dup_set:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                dup_set.add((i + 1, j))

            # add i, j+1 value set
            if j + 1 < len(nums2) and (i, j + 1) not in dup_set:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                dup_set.add((i, j + 1))
        return answer
