"""
link: https://leetcode.com/problems/merge-intervals/submissions/1932852366/?envType=problem-list-v2&envId=dsa-sorting-plateau-sorting
"""

from typing import List


# time: O(n log n) space: O(n)
# time analysis: sorting the intervals takes O(n log n), and merging takes O(n)
# space analysis: in the worst case, all intervals are non-overlapping, so we need O(n) space to store the merged intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # initialize merged list with the first interval
        merged = [intervals[0]]

        # loop through the sorted intervals and merge overlapping intervals
        for current in intervals[1:]:
            last = merged[-1]

            # if the current interval overlaps with the last merged interval, merge them by updating the end time of the last merged interval
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            # if the current interval does not overlap, add it to the merged list
            else:
                merged.append(current)

        return merged
